from collections import namedtuple
from pprint import pprint
subspells = dict((
    ('dai', 5),
    ('jee', 3),
    ('ain', 3),
    ('je', 2),
    ('ne', 2),
    ('ai', 2),
    ('fe', 1),
))
start_with, end_with, chunk_size = 'fe', 'ai', sum(sorted(map(len, subspells.keys()), reverse=True)[:2])
shortest_subspell = sorted(map(len, subspells.keys()))[0]

def damage(spell):
    """
    Function calculating damage
    :param str spell: string with spell
    :rtype: int
    :return: points of damage """
    global chunk_size, start_with, end_with
    
    if len(spell.split('fe')) != 2:
        return 0
    
    try:
        spell = spell[spell.index(start_with):]
        spell = spell[0:spell.rfind(end_with)+len(end_with)]
    except IndexError:
        return 0
    
    tree = branch_subspells(spell)
    best_damage = find_optimal_path_value(tree)
    return max(0, best_damage)

Branch = namedtuple('Branch', ['spell', 'value', 'length', 'path_value'])
NO_SUBSPELL = Branch(spell=None, value=-1, length=1, path_value=0)    
def branch_subspells(chunk, current_value=0):
    global subspells, end_with, NO_SUBSPELL, shortest_subspell
    if len(chunk) < shortest_subspell:
        return []
        
    tree = []
    for name, value in subspells.items():
        end = len(name)
        candidate = chunk[:end]
        if candidate != name:
            continue
            
        path_value = current_value + value
        branches = [Branch(name, value, len(name), path_value)] + branch_subspells(chunk[end:], path_value)
        tree.append(branches)
        
    if not len(tree):
        tree.append([NO_SUBSPELL] + branch_subspells(chunk[1:], current_value + NO_SUBSPELL.value))
            
    return tree

def find_optimal_path_value(tree):
    final_leafs = []
    
    stack = tree[:]
    while len(stack):
        branch = stack.pop()
        if len(branch) > 1:
            stack += branch[1:]
        else:
            final_leafs.append(branch[0])
            
    return max([b.path_value for b in final_leafs])

damage('xxxxxfejejeeaindaiyaiaixxxxxx')
