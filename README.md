## Use

**module#/** - weekly modules for University of Cincinnati's STAT2037 class

**utils/webassign.py** - easily parse the red Webassign data into an Python list 

**stats.py** - contains functions for calculating the following on lists of numbers:

- frequency
- mean
- median
- range
- significant figures of decimals
- rounding arrays to an interval

**template_problem.py** - good starting point for most Webassign problems, contains some imports
and other defaults. Copy to another folder (like module#).

## Documentation

Run in your terminal:

```pydoc utils/webassign```

```pydoc stats```

## Testing

Use 'doctest':

```python -m doctest utils/webassign.py```

```python -m doctest stats.py```
