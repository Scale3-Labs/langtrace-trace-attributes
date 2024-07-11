# Description

Please include a summary of the changes and the related issue to help is review the PR better and faster.

# Checklist for EVERY version bump:

- [ ] Ran [generate_python.sh](../scripts/generate_python.sh) to generate python models. (Check [README.md](../README.md) for instructions)
- [ ] Ran [generate_typescript.sh](../scripts/generate_typescript.sh) to generate typescript models. (Check [README.md](../README.md) for instructions)
- [ ] Ran `black .` to format the python code.
- [ ] Updated version in [setup.py](../setup.py) for python package.
- [ ] Updated version in [package.json](../src/typescript/package.json) for typescript package.
