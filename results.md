# Results

## 📊 Simulation Output

The distributed deadlock detection simulation was successfully executed using different configurations of sites, processes, and resources.

### 🔹 Parameters Used
- Number of Sites: 3  
- Processes per Site: 3  
- Resources per Site: 2  
- Simulation Duration: 40 units  

---

## 📈 Observations

### 1. Process Execution
- Processes continuously requested and released resources.
- When a resource was unavailable, processes entered a blocked state.

### 2. Wait-For Graph (WFG)
- Local WFGs were constructed at each site.
- A global WFG was formed by combining all local graphs.
- Edges represented dependencies between processes.

### 3. Deadlock Detection
- Cycles were detected in the global Wait-For Graph.
- Presence of cycles indicated deadlock conditions.

Example detected cycle:
