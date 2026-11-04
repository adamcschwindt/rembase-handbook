---
title: Production Run
subtitle: Build kits and packs, and enter what you built
slug: production-run
order: 10
---

## What this page is for

A **production run** is one job where we build a product from its parts. Example: a 2-pack is built from two single items.

**Who uses it:** Chad and Sabith on the floor. Becca plans the runs.

::: warn
All production runs are done in **RemBase**, not in Fishbowl. See [Next week in RemBase](next-week.html). To practice, use **your own practice run** (TEST-PRACTICE-RUN-BECCA, -CHAD or -SABITH).

**Press Finish Run once**, only when the run is built and the cartons are entered.
:::

## Sub-pages

| Sub-page | What it is for |
|---|---|
| **Production Run** | The office view: plan, components and lots. |
| **Production Run - Floor** | The floor view: what you built, cartons and pallet. |

## Task: find a run and check its parts

1. Click **Production Run** in the menu. The list shows real runs only.
2. Click the run in the list. **Rush** runs come first, then the soonest due date.
3. Check **Qty Planned**. This is how many to build.
4. Check **Output Part**. This is the product you build.
5. Scroll down to **Run Components**. It is above **Run Cartons**.
   - **Component Part SKU:** each part you need.
   - **Qty To Consume:** how many of that part.
   - **Suggested Lot Label:** the lot RemBase suggests: the one that expires first.
   - **Chosen Lot:** the lot to take. RemBase fills in the suggested lot. To take another lot, pick it in **Chosen Lot**. Only lots of that part with stock show.
6. **Run Cartons** shows the boxes after the floor enters them.
7. **Finished lots (filled at Finish)** shows the lots RemBase makes when the run is finished.

::: warn
If **Run Components** is empty, RemBase has no recipe for this product. Do not build. Tell Chad.
:::

## Task: send finished stock without prep (Becca)

For a product with **Warehouse Ready Qty** (finished, ready to ship):

1. Make the run as usual (Run Planning, Commit).
2. Open the run on **Production Run**. Tick **Pack only (ready stock)** (under **Rush**).
3. RemBase uses only ready lots. Nothing is prepped. The warehouse boxes it and presses **Finish Run**.

## Task: change the due date or put a run first (Becca)

1. Click **Production Run** in the menu.
2. Click the run in the list.
3. To change the due date: change **Date Needed (change if needed)** near the top. The **Due Date** lower down follows by itself.
4. To put the run first: tick **Rush**.

Both run lists (**Production Run** and **Production Run - Floor**) show Rush runs first. On the Floor page you see **Rush**, but you cannot change it.


## Task: enter what you built (Floor page)

1. Click **Production Run - Floor** in the menu.
2. Click your run in the list.
   The product card (**Output Part**) shows **Box To Use** (which box, or **No box**) and **Packing Notes** (what else to pack, for example labels). Tap the card to open the product.

   ![Floor page with Qty Built and the Pick list](img/pr-03-floor.png)

3. Read the **Pick list** (above **Run Cartons**). For each part it shows:
   - **Component Part SKU:** the part.
   - **Qty To Consume:** how many to take.
   - **Chosen Lot:** the lot to take. RemBase chose the lot that expires first.
   - **Chosen Lot Label:** the expiration date, the lot, how many are left, and the bin.

   Take that lot from that bin. To take a different lot: tap the **Chosen Lot** box and pick the lot. Only lots of that part with stock show. You cannot change anything else in the pick list.

   **The Pick list is empty?** RemBase has no recipe for this product. Do **not** press **Finish Run**. Tell Becca.
4. Build. Type the number you built in **Qty Built** (6).
5. In **Run Performed By** (under **Qty Built**), pick your name.
6. In **Run Cartons** (below the **Pick list**), click the **+** to add a carton row.
7. Fill in the row. Press **Tab** to go to the next box:
   - **Boxes:** how many boxes of this size.
   - **Units Per Box:** how many units in each box.
   - **Length**, **Width**, **Height:** box size in inches.
   - **Weight Per Box (lb):** weight of one full box in pounds.
8. If you have boxes of different sizes, add one row per size.
9. If you built fewer than planned, choose a **Short-Close Reason** and write a **Short-Close Note**.

## What you should see

![Floor page after typing the built quantity and cartons](img/pr-04-filled.png)

- **Qty Built** shows your number.
- **Run Stage** changes to **In Progress**.
- **Units** in Run Cartons = Boxes × Units Per Box. It should match Qty Built.
- **Missing** is empty when the carton row is complete.

## Task: finish the run

When the run is built and the cartons are entered, **Finish Run** takes the parts out of stock and adds the finished product. On a real run it also adds the units to the next Amazon shipment.

**Practice:** you may press Finish Run on **your own practice run**. Your practice run is not linked to any Amazon shipment, and its **Staging Pallet** is **TEST-BIN**, so the finished TEST kits go to TEST-BIN. Do not change the Staging Pallet.

1. Check **Qty Built** and the **Run Cartons** again.
2. Click **Finish Run** at the top right. Press it **once**.
3. Read **Finish Result**:
   - **DONE …** – the run is finished.
   - **NOT DONE: …** – nothing was changed. The message says what to fix, for example "add the cartons" or "the cartons hold 4 units but Qty built is 2". Fix it and press Finish Run again.

   **Finish Run may refuse. Then read Finish Result:**

   | Finish Result says | What to do |
   |---|---|
   | **the chosen lot still needs prep …** | That lot is not ready. Choose a ready lot in **Chosen Lot**, or ask Becca to clear it. Then press **Finish Run** again. |
   | **choose the lot for: …** | That part has no lot (for example, none was in stock when the run was made). Choose a lot for it in **Chosen Lot** in the **Pick list**, or ask Becca. Then press **Finish Run** again. |
   | **… Check the number. If it is right, ask the office to raise Qty Planned first.** | **Qty Built** is more than 110% of **Qty Planned**. Count again. If it is right, ask Becca to raise **Qty Planned**. |
   | **this run has no Date Needed …** | Ask Becca to fill in **Date Needed (change if needed)**. Then press **Finish Run** again. |

   The 110% limit is in Settings. Becca can change it.

- **Reverse Run** undoes a finished run. Anyone in the warehouse may reverse a run. The button is on the **Production Run** page, not on the Floor page:
  1. Click **Production Run** in the menu. Click the run.
  2. At the top, type why in **Run Reverse Reason (type it before Reverse Run)**.
  3. Press **Reverse Run** **once**. Read **Finish Result**.

  RemBase copies your reason into **Finish Result**. Without a reason, Reverse Run is refused.

## Common mistakes

- **Pressing Finish Run twice.** Press once and read **Finish Result**.
- **Units do not match Qty Built.** Check Boxes × Units Per Box.
- **Weight of the whole stack instead of one box.** Type the weight of one box.
- **Taking a different lot without changing Chosen Lot.** Change **Chosen Lot** first, or take the lot RemBase picked.
