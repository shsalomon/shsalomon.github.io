---
title: "SPREAD: Sampling-based Pareto front Refinement via Efficient Adaptive Diffusion"
excerpt: "SPREAD learns a conditional diffusion model over decision variables and then iteratively refines sampled candidates during reverse diffusion to move them toward Pareto-optimal regions.<br/><img src='/images/ZDT2_n200_online_resized.gif'>"
collection: portfolio
---

[SPREAD](https://github.com/safe-autonomous-systems/moo-spread) learns a conditional diffusion model over decision variables and then iteratively refines sampled candidates during reverse diffusion to move them toward Pareto-optimal regions. 
At each step, it guides the samples using adaptive multiple-gradient-descent directions to improve objectives while adding a repulsion term to maintain diversity along the Pareto front.

See the [project page](https://safe-autonomous-systems.github.io/moo-spread) for more details.

<p align="center">
  <img src="/images/spread_overview.png" alt="spread overview" width="700">
</p>
