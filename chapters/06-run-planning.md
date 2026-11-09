---
title: Run Planning
subtitle: Decide what to build next
slug: run-planning
order: 9
---

## What this page is for

Run Planning shows which products we should build and send to Amazon next.

**Who uses it:** Becca and Adam decide. Chad can read it to see what is coming.

## The list

**Run Planning** is the first page in the menu. The list is **grouped by Planning Vendor**: each vendor has its own block with a count. Find your products inside the block.

Each row shows how many we sold, what is at Amazon, and **Recommended Send Qty**. The column **Recommended Send Why** explains the number in one line.

The three columns you use are **Recommended Send Qty**, **Run Planning Override Qty** and **Run Planning Add To Run**. They sit side by side.

- **1 – Recommended Send Qty:** how many the system suggests we build and send. It plans enough stock at Amazon for **45 days**, plus the days Amazon needs to receive a shipment (about **12 days** now; RemBase updates this every day). The list is sorted by this number.
- **2 – Run Planning Override Qty:** Becca types her own number here to replace the suggestion.
- **3 – Run Planning Add To Run:** tick to put this product in the next runs.
- **Max Available to Build:** (scroll right) how many we **could** build with the parts we have now.
- **Days Of Cover FBA:** how many days the stock at Amazon will last. Blank, with 0 at Amazon, means the part is no longer in Amazon's report. See [Inventory](inventory.html).
- **Warehouse On Hand Qty:** all units of this product in our warehouse.
- **Warehouse Ready Qty:** finished units. They can ship now.
- **Warehouse Needs Prep Qty:** raw units. They need prep (label, sticker) before they can ship. Plan a prep run first.
  Example: a product shows **Ready 0** and **Needs prep 120**. Nothing can ship yet. Make a prep run for it first.

::: note
**Max Available to Build is not stock.** For a pack, it is how many packs the parts can make. For a single part that goes into packs, it is what is left after the packs take their share.
:::

The numbers update every hour. During the update some rows can show different times. Wait a few minutes and look again.

## Commit the runs (Becca only)

Commit has its own page, **Run Planning – Commit**.

1. On **Run Planning**, tick **Run Planning Add To Run** on each product (type **Run Planning Override Qty** first if you want your own number).
2. Press **Commit staged runs** (top of the page). This only opens the **Run Planning – Commit** page. It does not make any run.

![Run Planning – Commit page: the parts list](img/rp-01-list.png)

On **Run Planning – Commit**:

- **Staged for commit** (top right) lists the products you ticked. Check it first.
- **Commit Run Planning** makes production runs from the ticked rows right away. Read the result line under the button.
- **Clear Run Planning** removes all the ticks. **Staged for commit** is then empty.
- **Planned runs** (below the buttons) lists the open runs, with their **Run Stage**. TEST runs are not shown here.

The page says: **Commit makes the runs right away. Check 'Staged for commit' first. Clear empties the staged list.**

Do not press these unless you are Becca.

## Common mistakes

- **Reading Max Available to Build as stock.** It is not stock.
- **Ticking Add To Run to "try it".** The ticks are shared. Becca's next commit would use them.
- **Thinking a number is wrong during the hourly update.** Wait a few minutes.
