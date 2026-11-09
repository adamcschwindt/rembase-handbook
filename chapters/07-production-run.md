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
| **DESK: Production planning** (in **Production Run (Desk)**) | The office view (Becca): plan, lot lines, Reverse Run. |
| **FLOOR: Runs to do** (in **Production Run (Floor)**) | The floor view (Chad, Sabith): pick list, boxes, Finish Run. |

## Task: find a run and check its parts

1. Click **Production Run (Desk)** in the menu. The list shows real runs only.
2. Click the run in the list. **Rush** runs come first, then the soonest due date.
3. Check **Qty Planned**. This is how many to build.
4. Check **Output Part**. This is the product you build.
5. Scroll down to **Lot lines (pick list)** (read only) and **Run Components**. The floor ticks **Picked** on each line.
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

1. Make the run as usual (on Run Planning, tick the product, then press **Commit Run Planning**).
2. Open the run on **Production Run**. Tick **Pack only (ready stock)** (under **Rush**).
3. RemBase uses only ready lots. Nothing is prepped. The warehouse boxes it and presses **Finish Run**.

## Task: change the due date or put a run first (Becca)

1. Click **Production Run (Desk)** in the menu, then **DESK: Production planning**.
2. Click the run in the list.
3. To change the due date: change **Date Needed (change if needed)** near the top. The **Due Date** lower down follows by itself.
4. To put the run first: tick **Rush**.

Both run lists (**DESK: Production planning** and **FLOOR: Runs to do**) show Rush runs first, with a red flag. On the floor page you see **Rush**, but you cannot change it.


## Task: build and finish a run (Floor page)

1. Click **Production Run (Floor)** in the menu, then **FLOOR: Runs to do**. The list opens on **To do**: **Rush** runs first (red flag), then the soonest date. **Done** shows finished runs.
2. Click the run. The product card (**Output Part**) shows **Box To Use** and **Packing Notes**. Tap the card to open the product. **Pack only** on the title means ready stock: no prep.
3. Read the **Pick list**. It has **one line per lot**: **Part SKU**, **Lot**, **Lot Exp** (expiration date), **Bin** and **Line Qty**. Take each line from its bin. Then tick **Picked**.
   - Need another lot? Change the **Lot** or **Line Qty** on the line, or add a line. The lot must be for this product, and the lines must add up to the run quantity. A changed or added line shows **OVERRIDE**.
   - **The Pick list is empty?** RemBase has no recipe for this product. Do **not** press **Finish Run**. Tell Becca.
4. In **Run Cartons**, add one row for each kind of box. Fill in **Boxes**, **Units Per Box**, size and **Weight Per Box (lb)**. Choose the **Pick Line** the box came from. Each pick line reads: run, **Exp** date, bin, quantity (for example, **R1000 · Exp 2030-01-31 · A-01 · 24**). **One expiration date per box**: keep each lot in its own boxes. If the lot has no date, type **Printed Expiration Date**.
5. **Qty built (from boxes)** adds up your boxes. Leave **Qty Built** empty to use it. Type **Qty Built** only if it is different.
6. In **Run Performed By**, pick your name.
7. If you built fewer than planned, choose a **Short-Close Reason** and write a **Short-Close Note**.
8. Press **Finish Run** **once**. Confirm. Read **Finish Result**.

## What you should see

- **Qty Built** shows your number.
- **Run Stage** changes to **In Progress**.
- **Units** in Run Cartons = Boxes × Units Per Box. It should match Qty Built.
- **Missing** is empty when the carton row is complete.

## Task: fix the boxes on a finished run (Floor page)

A wrong box row on a **Done** run? You can fix it.

1. Click **Production Run (Floor)** in the menu, then **FLOOR: Runs to do**. Click **Done**. Click the run.
2. In **Run Cartons**, fix the **Boxes**, **Units Per Box**, size or **Weight Per Box (lb)**.
3. The **total units must stay the same**. You cannot add or remove units here.
4. Need more units? Ask Becca for a new run.

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
   | **tick Picked on every pick line of … Not picked: …** | Tick **Picked** on each line you took. Or pick a **Short-Close Reason**. Then press **Finish Run** again. |
   | **the picked lines of … add up to X but N is needed** | You picked too little. Pick the rest, or ask the office. |
   | **… add up to X but only N is needed** | You picked too much. Untick the extra line, or pick a **Short-Close Reason**. |
   | **pick line … uses a lot that is not a lot of …** | Change the **Lot** on that line to a lot of this product. |
   | **pick line … uses a lot that still needs prep** | That lot is not ready. Change the **Lot** on that line. |
   | **pick line … needs A but the lot only has B left** | Fix the line. Tell Becca to press **Refresh FEFO** on the run. Then press **Finish Run** again. |
   | **carton row … is linked to a pick line that belongs to another run** | In that carton row, pick the line of **this** run. |
   | **Boxes say N, Qty built says M** | Fix one. Leave **Qty Built** empty to use the boxes. |
   | **… Check the number. If it is right, ask the office to raise Qty Planned first.** | **Qty Built** is more than 110% of **Qty Planned**. Count again. If it is right, ask Becca to raise **Qty Planned**. |
   | **this run has no Date Needed …** | Ask Becca to fill in **Date Needed (change if needed)**. Then press **Finish Run** again. |

   The 110% limit is in Settings. Becca can change it.

- **Reverse Run** undoes a finished run. Anyone in the warehouse may reverse a run. The button is on the **Production Run** page, not on the Floor page:
  1. Click **Production Run (Desk)** in the menu. Click the run.
  2. At the top, type why in **Run Reverse Reason (type it before Reverse Run)**.
  3. Press **Reverse Run** **once**. Read **Finish Result**.

  RemBase copies your reason into **Finish Result**. Without a reason, Reverse Run is refused.

## Common mistakes

- **Pressing Finish Run twice.** Press once and read **Finish Result**.
- **Units do not match Qty Built.** Check Boxes × Units Per Box.
- **Weight of the whole stack instead of one box.** Type the weight of one box.
- **Taking a different lot without changing the line.** Change the **Lot** on the pick line first, or take the lot RemBase picked.
