# Contributing to airport-infrastructure-analytics

Thanks for taking the time to contribute. This repository holds research-grade
analysis code, so contributions that keep results **reproducible** are the most
valuable.

## Quick start

```bash
git clone https://github.com/DongsooJung/airport-infrastructure-analytics.git
cd airport-infrastructure-analytics
python -m venv .venv && . .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Contribution flow

1. **Open an issue first** for anything larger than a bug fix.
2. **Branch** from `main`: `git checkout -b <topic>`.
3. **Keep the pipeline reproducible.** Scripts must write their outputs and the
   metadata needed to rebuild them (timestamps, source queries, file hashes).
4. **State your assumptions.** Analysis windows, control-group definitions, and
   data vintages must be stated in code and documentation.
5. **Open a PR** describing what changed and why.

## What the maintainer cares about

- **Honest scope.** If a function is a stub or an approximation, say so.
- **Identification discipline.** DID designs must state the parallel-trends
  assumption and how it was checked.
- **Data provenance.** Every published number must trace back to a source
  and a collection date.

## Reporting bugs

Open an issue with the exact command, the expected result, and the actual
result. For security concerns, follow `SECURITY.md` instead of the public
issue tracker.

## License

Contributions are accepted under the [MIT License](LICENSE).
