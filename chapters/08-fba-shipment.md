---
title: FBA Shipment
subtitle: Send stock to Amazon and print box labels
slug: fba-shipment
order: 11
---

## What this page is for

**FBA** means Amazon stores and ships our products. We send boxes to Amazon warehouses. This page plans those shipments, gets the labels and tracks what Amazon received.

**Who uses it:** anyone on the team. Chad usually prints the labels and packs the boxes.

::: warn
**The buttons on this page are REAL, not practice.** They talk to Amazon for a real shipment.

- **Confirm placement** and **Confirm freight** cost money. Check the price first.
- Press a button **once**. Then wait until **Inbound Pending** is empty again (1-2 minutes).
- Not sure? Ask Adam before you press.
:::

## Sub-pages

| Sub-page | What it is for |
|---|---|
| **Sent to Amazon** | Every shipment we sent, and how much Amazon received. |
| **Next shipment** | The shipment we are building now. Labels are here. |
| **Sent from this plan** | The lines that went out with the last plan. |

## Task: check a shipment we sent

1. Click **FBA Shipment** in the menu.
2. Click **Sent to Amazon** (1).
3. Click a shipment in the list (2).

   ![List of shipments sent to Amazon, ids hidden](img/fba-01-sent.png)

4. Read the numbers:

   ![One shipment with its numbers](img/fba-02-detail.png)

   - **Status:** Shipped, Receiving, Closed or Cancelled.
   - **Total Units:** how many we sent.
   - **Qty Received By Amazon** (3): how many Amazon has counted.
   - **Qty Remaining:** how many Amazon has not counted yet.
   - **FBA Shipment Lines** (4): one line per product.
   - **Export Transfer For Fishbowl**, **Fishbowl Transfer File**, **Fishbowl Transfer Note:** the Fishbowl transfer for this shipment. See [Make the Fishbowl transfer file](#task-make-the-fishbowl-transfer-file).

## The Next shipment page

![Next shipment page with its main fields and buttons](img/fba-03-next.png)

Read it from top to bottom:

- **A – Inbound Pending:** a button was pressed and RemBase is working on it. Wait.
- **B – Result (after a button: wait 1-2 min):** the last message from RemBase. It tells you the next step. While Amazon is working it says what is happening, for example "Getting carrier quotes from Amazon. This takes a few minutes." Wait until it changes.
- **C – Mark Sent Result:** what **Mark as sent** did: **SENT …** or **NOT DONE …**.
- **D – 6. Labels (box + pallet):** the box labels, pallet labels and Bill of Lading (BOL). The file names say which is which: **box-labels** (on every box), **pallet-labels** (on every pallet), **bill-of-lading** (the paper for the carrier).
- **Ship Date:** the day the boxes are ready for carrier pickup (Amazon's ready date). Today or later.
- **Freight Class:** shipping details.
- **Freight Mode:** **LTL (pallets)** (a truck) or **Small parcel**. Read only.
- **Approved Placement Price**, **Approved Carrier Total:** what Amazon and the carrier charge.
- **Sent as (FBA IDs): type only if RemBase says no FBA shipment ID yet:** type the ID here only when **Mark Sent Result** says **NOT DONE: no FBA shipment ID yet**.

Below, the parts of the page are numbered in the order you use them:

- **1. Lines and boxes:** each line: **Part**, **Qty**, **Boxes**, **Expiry** and **Pallet**. To keep a line off this shipment, tick **Hold (not this shipment)** and write why in **Hold note**. When you press **Mark as sent**, a held line moves to the next shipment.
- **2. Pallets:** the pallets: size, weight, and "not stackable".
- **3. Create plan:** the button at the top.
- **4. Pick a warehouse, then ... > Confirm placement:** the Amazon warehouse choices, with their fee.
- **5. Pick a carrier, then ... > Confirm freight:** the carrier choices, with their price.
- **6. Labels (box + pallet):** the labels and the BOL.
- **7. Mark as sent:** the button at the top.

## Task: print the box labels

1. Open **FBA Shipment → Next shipment**.
2. Read **Result (after a button: wait 1-2 min)**. It says when the labels are ready.
3. Under **6. Labels (box + pallet)**, click the file you need. The files come in two steps:
   - After **Confirm placement**: the two **box label** files.
   - After **Confirm freight** (truck / LTL shipments only): the **pallet labels** and the **bill of lading**.

   The files:
   - **box labels letter 6-up** – six labels on one letter page.
   - **box labels 4x6 thermal** – for the label printer.
   - **pallet labels** – Amazon gives **four labels for each pallet**, one for each side.
   - **bill of lading** – the paper for the truck driver.
4. The file opens. Print it.
5. Put one box label on every box. Do not cover other labels.
6. Put the four pallet labels on the four sides of each pallet.

## Task: make the Fishbowl transfer file

Do this right after **Mark as sent**, on the shipment you just sent. Never on an older shipment: it may already be in Fishbowl.

1. Click **FBA Shipment → Sent to Amazon**.
2. Click the shipment you just sent.
3. Tick **Export Transfer For Fishbowl** **once**.
4. Wait 5 minutes. The tick clears by itself.
5. Read **Fishbowl Transfer Note**:

| Fishbowl Transfer Note says | What to do |
|---|---|
| **Exported …** | The file is in **Fishbowl Transfer File**. If Amazon split the shipment, there is one file for each FBA shipment ID. Tell Adam. |
| **CHECK the stock first** (under **Exported**) | The warehouse may not have enough. Tell Adam. |
| **NOT exported …** | No file was made. Tell Adam. |
| **The file could not be attached …** | Tick the box again in a few minutes. |

**Adam** imports each file in Fishbowl (**Import > Transfer Order**). Do **not** make the transfer in Fishbowl yourself.

## Sent from this plan

**FBA Shipment → Sent from this plan** lists each product line that went out with the last plan: how many units, when, and which Amazon shipment it went in. It is read-only.

![Lines sent from the last plan, ids hidden](img/fba-04-sent-from-plan.png)

## The buttons, in order (real buttons: be careful)

Anyone on the team may press these for a real shipment. They work on any **open** shipment that is **not** a TEST shipment. Read what each one does first.

| Button | What it does |
|---|---|
| **Create plan** | Starts a new shipment plan with Amazon. |
| **Refresh options** | Asks Amazon again for warehouse choices. |
| **Confirm placement** | Accepts the Amazon warehouse choice. **Costs money.** |
| **Get prices again** | Asks carriers for new prices. Does not cost money. |
| **Confirm freight** | Books the carrier. **Costs money.** |
| **Re-check** | Asks Amazon for the latest status. |
| **Cancel plan** | Cancels the plan with Amazon. |
| **Mark as sent** | Tells RemBase the boxes left our building. |

Some buttons are inside the **…** menu at the top of the page.

![The shipment buttons in the … menu](img/fba-05-menu.png)

## What you should see

- After a button press, **Inbound Pending** shows a message, then clears.
- **Result (after a button: wait 1-2 min)** then says what happened and what to do next.
- After **Confirm placement**, the two box label files appear under **6. Labels (box + pallet)**.
- After **Confirm freight** (truck shipments), the pallet labels and the bill of lading appear too.

## Products with two Amazon SKUs

- Some products have two Amazon SKUs: the original and a **-stickered** or **-barcode** version. RemBase treats both as the same product. The stock is counted on the original product.
- Becca chooses the **one** SKU to ship under. In the **sku-map**, she ticks **Ship as** on that SKU.
- If a product has two active SKUs and not exactly one is ticked, the shipment stops. **Result** says **NOT DONE** and asks Becca to tick **Ship as**. Nothing is sent to Amazon until this is fixed.

## Common mistakes

- **Pressing a button twice because nothing seems to happen.** Wait for **Inbound Pending** to clear.
- **Using old labels.** Always print from the shipment you are packing.
- **Wrong label size.** Use 4x6 for the thermal printer and 6-up for normal paper.
- **Confirming without checking the price.** Confirm placement and Confirm freight cost money.
- **Practicing on this page.** These buttons are real. There is no TEST shipment.
- **Two Amazon SKUs with no Ship as tick.** The shipment stops until Becca ticks **Ship as** on one SKU.
