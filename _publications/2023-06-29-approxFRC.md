---
title: "Approximation Algorithms for Fair Range Clustering"
collection: Proceedings of the 40 th International Conference on Machine Learning, Honolulu, Hawaii, USA. PMLR 202, 2023
permalink: /publications/2023-approxFRC
excerpt: 'Approximation Algorithms for Fair Range Clustering'
date: 2023-06-29
venue: 'ICML 2023'
citation: 'Hotegni, S.S., Mahabadi, S. and Vakilian, A., 2023, July. Approximation Algorithms for Fair Range Clustering. In International Conference on Machine Learning (pp. 13270-13284). PMLR.'
---

This paper studies the fair range clustering problem in which the data points are from different demographic groups and the goal is to pick `k`
centers with the minimum clustering cost such that each group is at least minimally represented in the centers set and no group dominates the
centers set. More precisely, given a set of `n` points in a metric space `(P, d)` where each point belongs to one of the ℓ different demographics
`(i.e., P = P1 ⊎ P2 ⊎ · · · ⊎ Pℓ)` and a set of `ℓ` intervals `[α1, β1], · · · , [αℓ, βℓ]` on desired number of centers from each group, the goal is to pick a set of k centers `C` with minimum `ℓp-clustering` cost such that for each group `i ∈ ℓ, |C ∩ Pi| ∈ [αi, βi]`. In particular, the fair range `ℓp-clustering` captures fair range `k-center`, `k-median` and `k-means` as its special cases. In this work, we provide an efficient constant factor approximation algorithm for the fair range `ℓp-clustering` for all values of `p ∈ [1, ∞)`.


[Download paper here](https://openreview.net/pdf?id=gBoKJT5JhM)
