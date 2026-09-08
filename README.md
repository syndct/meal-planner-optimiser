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

## Literature
- OptiMUS: Scalable Optimization Modeling with (MI)LP Solvers and Large Language Models
    - [Paper](https://arxiv.org/abs/2402.10172)
    - [Github](https://github.com/teshnizi/OptiMUS)
- OR-LLM-Agent: Automating Modeling and Solving of Operations Research Optimization Problems with Reasoning LLM
    - [Paper](https://arxiv.org/abs/2503.10009)
- OPTIAGENT: A Physics-Driven Agentic Framework for Automated Optical Design
    - [Paper](https://arxiv.org/abs/2602.23761)
- NL4Opt Competition: Formulating Optimization Problems Based on Their Natural Language Descriptions
    - [Paper](https://arxiv.org/abs/2303.08233)
    - [Github](https://github.com/nl4opt/nl4opt-competition)