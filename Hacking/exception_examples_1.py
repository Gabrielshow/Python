#rigorous error checking of #sum function implementation
#for some reason this gives in an error of iterable attribute not in the module collections
# It is a work in progress code
# expressing the advanced idea of advanced exception Handling
import collections
def sum(values):
    if not isinstance(values, collections.Iterable):
        raise TypeError('parameter must be an iterable type')
    total = 0
    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError('elements must be numeric')
        total = total + v
    return total