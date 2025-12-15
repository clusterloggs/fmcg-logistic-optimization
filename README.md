# FMCG Logistics Optimization Project (Greedy Knapsack)

## Project Overview

This project demonstrates how **greedy optimization (knapsack heuristics)** can be applied to **FMCG logistics in Nigeria**, focusing on **truck loading and distribution decisions** under capacity constraints.

The scenario is intentionally realistic and mirrors challenges faced by Nigerian FMCG distributors such as Dangote Group, Nestlé Nigeria, Nigerian Breweries, and regional distributors supplying retail outlets across Lagos, Ibadan, and Ogun State.


## Business Problem

A Nigerian FMCG distributor operates daily truck deliveries from a **Lagos distribution center**. Each truck has limited **volume capacity**.

On a given day, multiple SKUs compete for truck space. Each SKU has:

* Expected profit contribution
* Required truck volume (cartons / pallet space)

**Objective:**
Maximize total profit loaded onto the truck without exceeding capacity.

This is a classic **0/1 knapsack problem**, solved here using **greedy heuristics** for real-time decision-making.


## Assumptions

* Single truck per run
* No SKU splitting (either loaded or not)
* Volume is the binding constraint (not weight)
* Profit values are estimated from historical sales


## Sample Output Interpretation

* **Profit-based greedy** favors high-margin beverages but may waste space
* **Volume-based greedy** loads many small SKUs with mediocre returns
* **Density-based greedy** consistently delivers the highest profit per truck



## Business Insights

1. Greedy heuristics are effective for **same-day dispatch decisions**
2. Density-based allocation aligns with **profit-per-cubic-meter KPIs**
3. The model is fast, interpretable, and easy to operationalize



## Limitations

* Not globally optimal for 0/1 knapsack
* Ignores routing and multi-drop constraints
* Assumes accurate profit forecasts



## Possible Extensions

* Multi-truck allocation
* Weight + volume constraints
* Demand uncertainty simulation
* Comparison with dynamic programming or MIP

