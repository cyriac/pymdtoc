<!-- starttoc -->
# Table of contents
- [mdTOC](#mdtoc)
    - [Installation](#installation)
    - [Usage](#usage)
        - [Generate TOC](#generate-toc)
        - [Generate and update file](#generate-and-update-file)
    - [Via python](#via-python)
        - [Optional arguments](#optional-arguments)

<!-- endtoc -->

# mdTOC

Create Table of contents for markdown files

## Installation
```shell
pip install pymdtoc
```


## Usage

### Generate TOC
```shell
mdtoc generate filename.md
```

### Generate and update file
```shell
mdtoc inplace filname.md
```

## Via python

```python
from pymdtoc import TOC
toc = TOC(file="filename.md")
print(toc.toc)
print(toc.content)
```

### Optional arguments

- `toc_heading` - Table of contents heading (str)
- `anchor_function` - Ability to provide custom anchor tag generator

