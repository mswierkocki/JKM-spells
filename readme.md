Method calculating damage done by a spell of the famous polish wizard.
Eg.  - '[fejejeeaindaiyaiai](https://www.youtube.com/watch?v=XkeVYHJ6AG8)' 

Spell consists of subspells. Each subspell add points of damage respectively:

### 'fe' - 1 'je' - 2 'jee' - 3 'ain'- 3 'dai'- 5 'ne' - 2 'ai'- 2

Spell start with 'fe' and end with 'ai'. Spell body can have subspells or other letters, but every single letter (not in a subspell)  damage of decrease spell by 1 point. 'fe' can occur only once and 'ai' always end the spell.
If you can use different sets of subspells in spell, choose the one with the biggest damage (in example fedaineai: fe-dai-ne-ai: 2+5+2+2, not fe-d-ain-e-ai 2-1+3-1+2).

Method return 0 if damage is negative or if spell is incorrect.
# Correct spells: 
    'xxxxxfejejeeaindaiyaiaixxxxxx' 
    (fe-je-jee-ain-ai-ai-ai) 'jejefeai' (fe-ai) 
# Incorrect spells:
    'jejeai' (doesn't start with 'fe') 'dadsafeokokok' (doesn't end with 'ai') 'aioooofe'

### Example
```python
 damage('feeai') == 2
 damage('feaineain') == 1 + 2 + 2 + 2 = 7 (fe-ai-ne-ai) - not (fe-ain-ai) because 1+3+2 = 6 
 damage('jee') == 0 
 damage('fefefefefeaiaiaiaiai') == 0 (more than one 'fe') 
 damage(fdafafeajain) == 1 (fe-ai) 3 - 2 (because 'aj') 
 damage('fexxxxxxxxxxai') == 0 (3-10 = -7 < 0)
```

