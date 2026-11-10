---
title: Next week in RemBase
subtitle: Production runs, the pallet shipment, and counts are real in RemBase
slug: next-week
order: 0
---

## What is new next week

These are now **real** in RemBase:

- **All production runs** (prep runs and runs with a recipe). Becca sets them up. The warehouse builds them. None are made in Fishbowl.
- **An Amazon pallet shipment.** Chad or Sabith plan it, label it and send it in RemBase. Adam imports the transfer into Fishbowl.
- **Bin counts, stock moves and receiving with RemBase Scan.** Counts and moves go to Fishbowl by themselves. Adam imports the day's receipts into Fishbowl.

::: warn
**One system only.** A run, a shipment, a count, a move or a receipt you do in RemBase, you do **not** also do in Fishbowl. Never do the same work twice.
:::

Everything else stays the same until December 1: other real work goes in **Fishbowl**.

## A. Becca: set up a prep run, step by step

A **prep run** gets an item ready for Amazon (label, sticker). It has no recipe.

::: warn
**All runs are in RemBase from today**, prep runs too. Do **not** make them in Fishbowl.
:::

**First:** open **1. Plan runs** and check that **only** the products you want are ticked in **Add To Run**. Old ticks would be committed too.

1. Click **1. Plan runs** in the menu. Find the product (**PS**, **Danesi** and **Clear Conscience** groups are first). Check **Recommended Send**. If **Stock Alert** says **NEED MORE**, tell Adam. The next columns are **Override** and **Add To Run**.
2. To use your own number, type it in **Override**.
3. Tick **Add To Run**.
   When you tick **Add To Run** and **Override** is empty, RemBase fills it with **Recommended Send**. Change the number if you want a different one. A number you typed is never changed.
4. Press **Commit staged runs** (top of the page). RemBase asks **Are you sure?** Press **Yes** **once**. Read the result line: **DONE: … run(s) made**.
5. Click **2. Runs - office** in the menu, then **Office: dates, rush, reverse**. Click the new run.
6. Check **Run Components**. A prep run has **one** row: the product itself. (A run with a recipe shows its parts.) If **Run Components** is empty, stop and tell Adam.
7. Check **Lot lines (pick list)**. RemBase chose the lots that expire first. The warehouse can change a lot on the floor page. No lines means no stock when you pressed Commit staged runs.
8. **Date Needed (change if needed)** is 7 days from today. Change it if needed. Do not leave it empty.
9. If the run is urgent, tick **Rush** (on **1. Plan runs** or on the run). Rush runs are at the top of the Floor page.

Do **not** make this run in Fishbowl (no work order). When the warehouse presses **Finish Run**, RemBase tells Fishbowl by itself.

A run with a recipe (a kit or a pack) has the same steps.

**Finished stock that needs no prep** (**Warehouse Ready Qty**): make the run the same way, and tick **Pack only (ready stock)** on the run. RemBase uses only ready lots. The warehouse boxes it and presses **Finish Run**.

## B. Warehouse: build the run and count

**Build the run (Chad, Sabith):**

1. Click **3. Runs - warehouse floor** in the menu, then **Floor: pick, pack, finish**. **Rush** runs are at the top (red flag).
2. Click the run. The product card shows **Box To Use** and **Packing Notes**. Tap it to open the product.
3. Read the **Pick list**: one line per lot (**Part SKU**, **Lot**, **Lot Exp**, **Bin**, **Line Qty**). Take each line from its bin and tick **Picked**. Need another lot? Change the **Lot** or **Line Qty**, or add a line. **The Pick list is empty?** Do **not** press **Finish Run**. Tell Becca.
4. In **Run Cartons**, add one row for each box size: **Boxes**, **Units Per Box**, size, **Weight Per Box (lb)** and the **Pick Line**. One expiration date per box. **Qty built (from boxes)** adds them up: leave **Qty Built** empty. In **Run Performed By**, pick your name.
5. Press **Finish Run** **once**. Read **Finish Result**.
   - **DONE …** – the run is finished. A prep run says **DONE: Moved …**: the items moved to the pallet.
   - **NOT DONE: …** – nothing changed. Fix what it says. Press **Finish Run** again.

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
7. Do **not** enter this run in Fishbowl.

See [Production Run](production-run.html) for more.

**Move stock between bins:** use **RemBase Scan**. See [Move stock with RemBase Scan](basics.html#move-stock-with-rembase-scan). Do **not** move it again in Fishbowl.

**Count bins:** use **RemBase Scan**, the same as now. Each count goes to Fishbowl by itself. A **red box** after a count means it waits for Becca or Adam: tap **OK**. See [How to scan](basics.html#how-to-scan).

**Receive deliveries:** on the floor with **RemBase Scan**. See [Receive a delivery with RemBase Scan](receiving.html#receive-a-delivery-with-rembase-scan). At a computer (office): the PO page, **Desk receiving**. See [Receive several lines on the PO page](receiving.html#task-receive-several-lines-on-the-po-page-office). Receive each delivery **once**, never also in Fishbowl.

## C. The pallet shipment to Amazon

The first real pallet shipment is on **Wednesday, November 11**, with Adam there. **Chad or Sabith** do every step below. **Adam** imports the Fishbowl transfer file.

::: warn
These buttons are **real**. **Confirm placement** and **Confirm freight** cost money. Press each button **once**. Then wait until **Inbound Pending** is empty (1-2 minutes).
:::

![Next shipment page with its main fields and buttons](img/fba-03-next.png)

The page parts have the same numbers as the steps below.

1. Open **FBA Shipment → Next shipment**. In **1. Lines and boxes**, check each line: **Part**, **Qty**, **Boxes**, **Expiry** and **Pallet**. A line that must not go on this truck: tick **Hold (not this shipment)** and write why in **Hold note**.
2. In **2. Pallets**, fill in each pallet: size, weight, "not stackable".
3. Press **Create plan** (top of the page). Wait. Read **Result (after a button: wait 1-2 min)**.
4. In **4. Pick a warehouse, then ... > Confirm placement**, check the Amazon warehouse choices and their fee. Then press **…** and **Confirm placement**.
5. In **5. Pick a carrier, then ... > Confirm freight**, check the carrier prices and the **Pickup Date**. If **Pickup Note** warns that the pickup is late, tick **Pickup OK** on the carrier you pick (only if that date is fine). Then press **…** and **Confirm freight**.
6. Print from **6. Labels (box + pallet)**:
   - the file with **box-labels** in its name: one label on every box (4x6 thermal printer);
   - the file with **pallet-labels**: four labels for each pallet, one on each side (4x6 thermal printer);
   - the file with **bill-of-lading** (BOL): for the driver.
7. When the truck has left: press **Mark as sent** (top of the page) **once**. Read **Mark Sent Result** (under the **Result** line):
   - **SENT …** – done. The next shipment is empty and ready.
   - **NOT DONE: no FBA shipment ID yet …** – type the Amazon shipment ID in **Sent as (FBA IDs)**. It starts with **FBA**. More than one: put a comma between them. Press **Mark as sent** again.
8. After **Mark as sent**, click **FBA Shipment → Sent to Amazon**. Click the shipment you just sent. Tick **Export Transfer For Fishbowl** **once**. Wait 5 minutes. The tick clears by itself. Read **Fishbowl Transfer Note**:

   | Fishbowl Transfer Note says | What to do |
   |---|---|
   | **Exported …** | The file is in **Fishbowl Transfer File**. If Amazon split the shipment, there is one file for each FBA shipment ID. Tell Adam. |
   | **CHECK the stock first** (under **Exported**) | The warehouse may not have enough. Tell Adam. |
   | **NOT exported …** | No file was made. Tell Adam. |
   | **The file could not be attached …** | Tick the box again in a few minutes. |

   **Adam** imports each file in Fishbowl (**Import > Transfer Order**) and ships the transfer there. Do **not** make the transfer in Fishbowl yourself.

See [FBA Shipment](fba-shipment.html) for each button.

## Who to ask

**Adam**, for anything about next week's run, shipment or counts.

## If something looks wrong

1. **Stop.** Do not press the button again.
2. Do **not** do it in Fishbowl instead.
3. Tell **Adam**: the page, the record, what you pressed and what you saw. A screenshot helps.
