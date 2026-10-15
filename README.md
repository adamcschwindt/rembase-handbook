# RemBase Handbook

Step-by-step help for RemBase, Remington Supply's inventory system.
Simple English, one action per step, a picture for every step.

## Rebuild the site

Needs `pandoc` and Python 3.

```bash
python3 build.py
```

- Chapters live in `chapters/*.md`. Each starts with a small block: title, subtitle, slug, order.
- Pictures live in `img/`. They are made outside this repo by the capture tools, and every one is checked before it is added here.
- `build.py` writes one `.html` page per chapter, `assets/search-index.js`, and checks that every picture a page uses exists.

## Rules for pictures

- Only redacted pictures go in `img/`.
- Prices, costs, vendor contacts, customer data, Amazon shipment and plan IDs, and system IDs are blacked out.
- Practice data only (TEST items) wherever a task changes data.
