# Dynamic incomplete IPFST incremental analysis

Public code and synthetic reproducibility materials for the manuscript on
incremental maintenance of AP1 pairwise conflict values.

## Contents

- model.py: Pythagorean fuzzy features, distances, endogenous weights and AP1 aggregation.
- generate_synthetic_demo.py: deterministic quarter-unit-disk data generator.
- data/: synthetic benchmark summaries; run the generator to create local
  reference outputs.
- data/benchmark_summary.csv: aggregate materialized-difference benchmark results.
- data/event_check_summary.csv: aggregate correctness and fallback checks.
- LICENSE: MIT license for original code.

Run the generator after installing requirements.txt.

## Data provenance and restrictions

The synthetic data and aggregate summaries are author-generated. Source-paper
table transcriptions, publication-specific completion targets and coalition
audits are intentionally excluded because the source article copyright page
states that Elsevier retains all rights. They must not be relabeled CC BY
without permission. The public files do not contain the source-paper table.

The benchmark summaries are aggregate results from the manuscript's local
runs. They do not constitute an official archive until a tagged Release is
created. Create a release, record its URL and commit SHA, and only then add
that URL to the manuscript. Zenodo can mint a DOI after GitHub integration.

This repository does not claim to provide genuine multi-round observations,
the external dynamic-baseline implementation, or a full 3x3 system.
Structural events are conservatively handled by full fallback.
