# meal-planner-optimiser
A meal planning tool that receives user inputs in the form of conversational data and frames it as an LP.

## Basic implementation for v0.1.0
**Chat**
- A local version of `llama3.2` on `Ollama`.
- Collect requirements through conversation (objective function, constraints, food preferences, etc.)

**Data**
- Open-source nutrition dataset.

**Optimizer**
- `pyomo` as the framework.
- `GLPK` as the solver.

**UI**
- `streamlist` app.