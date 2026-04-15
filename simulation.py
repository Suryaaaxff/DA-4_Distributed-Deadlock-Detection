import simpy
import networkx as nx
import random
from dataclasses import dataclass

@dataclass
class SimEvent:
    time: float
    event_type: str
    site_id: int
    process_id: int
    detail: str


class Site:
    def __init__(self, site_id, env, log):
        self.site_id = site_id
        self.env = env
        self.log = log
        self.resources = {}
        self.wfg = nx.DiGraph()

    def add_resource(self, r):
        self.resources[r] = None

    def request(self, p, r):
        if self.resources[r] is None:
            self.resources[r] = p
            self.log.append(SimEvent(self.env.now, "ACQUIRE", self.site_id, p, f"P{p} got R{r}"))
            return True
        else:
            holder = self.resources[r]
            self.wfg.add_edge(f"P{p}", f"P{holder}")
            self.log.append(SimEvent(self.env.now, "BLOCK", self.site_id, p, f"P{p} waits for P{holder}"))
            return False

    def release(self, p, r):
        if self.resources[r] == p:
            self.resources[r] = None
            self.log.append(SimEvent(self.env.now, "RELEASE", self.site_id, p, f"P{p} released R{r}"))


def process(env, pid, site, log):
    while True:
        # Only local resources → FIXED ERROR
        r = random.choice(list(site.resources.keys()))

        log.append(SimEvent(env.now, "REQUEST", site.site_id, pid, f"P{pid} requests R{r}"))

        if site.request(pid, r):
            yield env.timeout(random.uniform(1, 3))
            site.release(pid, r)
        else:
            yield env.timeout(2)

        yield env.timeout(1)


def run_simulation(
    num_sites=3,
    num_processes_per_site=3,
    num_resources_per_site=2,
    sim_duration=30
):
    env = simpy.Environment()
    log = []
    sites = {}

    # Create sites
    for i in range(num_sites):
        sites[i] = Site(i, env, log)

    # Create resources
    rid = 0
    for s in sites.values():
        for _ in range(num_resources_per_site):
            s.add_resource(rid)
            rid += 1

    # Create processes
    pid = 0
    for s in sites.values():
        for _ in range(num_processes_per_site):
            env.process(process(env, pid, s, log))
            pid += 1

    # Run simulation
    env.run(until=sim_duration)

    # Global WFG
    global_wfg = nx.DiGraph()
    for s in sites.values():
        global_wfg.add_edges_from(s.wfg.edges())

    # Detect cycles
    deadlocks = list(nx.simple_cycles(global_wfg))

    return {
        "log": log,
        "detected_deadlocks": deadlocks,
        "global_wfg": global_wfg
    }