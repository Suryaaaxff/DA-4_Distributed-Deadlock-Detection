# Distributed Deadlock Detection using Wait-For Graph (WFG)
VIDEO DEMONSTARTION LINK : https://drive.google.com/file/d/1nlb0Ut1nO6SjFc32JplEzufJSpYPoLni/view?usp=sharing

## 📌 Overview
This project implements a **Distributed Deadlock Detection Algorithm** using the **Wait-For Graph (WFG) model**. It simulates multiple processes competing for shared resources across multiple distributed sites using a **Discrete Event Simulation (DES)** approach with SimPy.

Each site maintains its own local Wait-For Graph, and a global deadlock is detected by identifying cycles across sites.

---

## 🎯 Objectives
- Simulate distributed systems with multiple sites and processes  
- Implement resource allocation and request handling  
- Construct **local and global Wait-For Graphs**  
- Detect deadlocks using **cycle detection algorithm**  
- Visualize system behavior using an interactive **Streamlit dashboard**

---

## ⚙️ Technologies Used
- **Python**
- **SimPy** → Discrete event simulation  
- **NetworkX** → Graph modeling and cycle detection  
- **Streamlit** → Web-based UI  
- **Matplotlib** → Graph visualization  
- **Pandas** → Data handling  

---

## 🧠 Concepts Implemented
- Distributed Systems  
- Deadlock Detection  
- Wait-For Graph (WFG)  
- Cycle Detection (Graph Theory)  
- Resource Allocation & Blocking  
- Discrete Event Simulation  

---

## 🏗️ System Architecture

### 1. Sites
- Each site contains:
  - Processes
  - Resources
  - Local Wait-For Graph

### 2. Processes
- Request resources  
- Wait if resource is busy  
- Create dependency edges in WFG  

### 3. Wait-For Graph
- Nodes → Processes  
- Edges → Dependency (P1 → P2 means P1 waits for P2)

### 4. Deadlock Detection
- Global WFG is constructed  
- Cycles are detected using NetworkX  
- If cycle exists → Deadlock  

---

## 🔄 Working Flow
1. Initialize multiple sites with resources  
2. Create processes for each site  
3. Processes request resources randomly  
4. If resource is unavailable:
   - Process is blocked  
   - Edge added in WFG  
5. Simulation runs using SimPy  
6. Global WFG is built  
7. Cycle detection is performed  
8. Results displayed in UI  

---

## 📊 Features
- ✅ Global Wait-For Graph visualization  
- ✅ Per-site WFG visualization  
- ✅ Deadlock detection output  
- ✅ Event log tracking  
- ✅ Resource allocation tables  
- ✅ Clean dashboard UI  

---

## 🖥️ How to Run

### Step 1: Clone Repository
```bash
git clone https://github.com/your-username/deadlock-detection.git
cd deadlock-detection
![Uploading image.png…]()
