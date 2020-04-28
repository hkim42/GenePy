# GenePy

GenePy is a Python port of miniEugene, a specification tool for exploring genetic designs based on user declared rules, which act as constraints for potential designs. For more information on miniEugene click [here](http://minieugene.cidarlab.org/index.html). To learn more about the Eugene ecosystem click [here](http://eugenecad.org/index.html).

## Setup
If not already setup, please install the latest version of Python3.

```bash
$ brew install python3
```

The only dependency GenePy requires is the `python-constraint` package.  `python-constraint` can be installed using `pip3`.

```bash
$ pip install python-constraint
```

## Usage

The following methods are available when using GenePy to implement Eugene rules and work with solutions.

### Counting Rules
* `contains(a)`
* `morethan(a,n)`
* `exactly(a,n)`
* `then(a,B)`
* `witH(a,B)`

### Positioning Rules
* `startswith(a)`
* `endswith(a)`
* `all_after(a, B)`
* `some_after(a,B)`
* `all_before(a,B)`
* `some_before(a,B)`
* `all_nextto(a,B)`
* `some_nextto(a,B)`

### Orientation Rules
* `all_forward_if(a)`
* `all_reverse_if(a)`
* `some_forward(a)`
* `some_reverse(a)`
* `all_forward()`
* `all_reverse()`

### Interaction Rules
* `represses(a,B)`
* `induces(a,B)`
* `drives(a,B)`

### General
* `generate(number=0)`
* `change_length(n)`
  * Must call `change_length()` before `generate()` in script
* `rulesToFile(filename)`
* `solutionsToFile(filename, number=0)`

## Examples

```python
from genepy import genepy

if __name__ == '__main__':
    # initiate class
    gp = genepy(10)

    # add user defined rules with rule methods
    gp.contains("p1")
    gp.contains("p2")
    gp.contains("p3")
    gp.exactly("p4", 2)
    gp.morethan("p5", 1)

    gp.some_before("p2", "p3")
    gp.endswith("p5")
    gp.startswith("p1")

    gp.induces("p1", "p3")
    gp.drives("p3", "p2")

    # print out generated solutions that satisfy rules
    print(gp.rules["induces"])
    outputs = gp.generate(5)

    for x in outputs:
        print(x)

    gp.solutionsToFile("test_solutions.json", 5)
    gp.rulesToFile("test_rules.json")
```
### Expected Output
```
{'p1': 'p3'}
{0: 'p1', 1: 'p4', 2: 'p4', 3: 'p3', 4: 'p3', 5: 'p3', 6: 'p2', 7: 'p3', 8: 'p5', 9: 'p5'}
{0: 'p1', 1: 'p4', 2: 'p4', 3: 'p3', 4: 'p3', 5: 'p3', 6: 'p2', 7: 'p5', 8: 'p3', 9: 'p5'}
{0: 'p1', 1: 'p4', 2: 'p4', 3: 'p3', 4: 'p3', 5: 'p3', 6: 'p5', 7: 'p2', 8: 'p3', 9: 'p5'}
{0: 'p1', 1: 'p4', 2: 'p4', 3: 'p3', 4: 'p3', 5: 'p2', 6: 'p3', 7: 'p3', 8: 'p5', 9: 'p5'}
{0: 'p1', 1: 'p4', 2: 'p4', 3: 'p3', 4: 'p3', 5: 'p2', 6: 'p3', 7: 'p2', 8: 'p5', 9: 'p5'}
```

## Limitations
GenePy currently requires additional development to address runtime as design length and rule occurrences increase. Further optimization is required to reduce runtime for more complex designs.
