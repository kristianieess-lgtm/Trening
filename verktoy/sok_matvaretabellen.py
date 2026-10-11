#!/usr/bin/env python3
"""Slå opp matvarer i Matvaretabellen (Mattilsynet) for å kontrollere ING-tabellen i dagbok.html.

Bruk:
  curl -sL -o foods.json https://www.matvaretabellen.no/api/nb/foods.json
  python3 -I sok_matvaretabellen.py foods.json "Cottage cheese" "Havregryn" "Brød, grovt"

Skriver kcal, protein, karbo, fett per 100 g og porsjonsvekter (stk, skive, dl ...).
Kjør med -I (isolert modus) siden foods.json er ekstern data."""
import json, sys

def val(food, nutrient):
    for c in food['constituents']:
        if c['nutrientId'] == nutrient:
            return c.get('quantity')

foods = json.load(open(sys.argv[1], encoding='utf-8'))['foods']
for q in sys.argv[2:]:
    hits = sorted((f for f in foods if q.lower() in f['foodName'].lower()), key=lambda f: len(f['foodName']))[:8]
    print('##', q, f'({len(hits)} treff)')
    for f in hits:
        portions = ', '.join(f"{p['portionName']} {p['quantity']:g} g" for p in f.get('portions', []))
        print(f"  {f['foodName'][:58]:58} {f['calories']['quantity']:>5} kcal  P {val(f,'Protein')}  K {val(f,'Karbo')}  F {val(f,'Fett')}   [{portions}]")
