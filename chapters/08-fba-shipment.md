---
title: FBA Shipment
subtitle: Send stock to Amazon and print box labels
slug: fba-shipment
order: 8
---

## What this page is for

**FBA** means Amazon stores and ships our products. We send boxes to Amazon warehouses. This page plans those shipments, gets the labels and tracks what Amazon received.

**Who uses it:**

- **Adam or Becca** press the buttons. Some buttons cost money.
- **Chad** prints the labels and packs the boxes.

::: warn
**Only Adam or Becca press buttons on this page.** Everyone else: look, print labels, and ask.
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

## The Next shipment page

![Next shipment page, ids, prices and labels hidden](img/fba-03-next.png)

Read it from top to bottom:

- **1 – Inbound Pending:** a button was pressed and RemBase is working on it. Wait.
- **2 – Inbound Result:** the last message from RemBase. It tells you the next step.
- **3 – Label Files:** the box labels, pallet labels and Bill of Lading (BOL).
- **Ship Date**, **Freight Class:** shipping details.
- **Approved Placement Price**, **Approved Carrier Total:** what Amazon and the carrier charge (hidden on this site).
- **FBA Shipment Lines** (bottom of the page): each product, how many units and how many boxes.

While a plan is in progress you also see:

- **Step 1** – a list of Amazon warehouse choices, with their fee.
- **Shipment Pallets** – the pallets: size, weight, and "not stackable".
- **Step 2** – a list of carrier choices, with their price.

## Task: print the box labels

1. Open **FBA Shipment → Next shipment**.
2. Read **Inbound Result**. It says when the labels are ready.
3. Under **Label Files**, click the file you need:
   - **box labels letter 6-up** – six labels on one letter page.
   - **box labels 4x6 thermal** – for the label printer.
   - **pallet labels** – one for each pallet.
   - **bill of lading** – the paper for the truck driver.
4. The file opens. Print it.
5. Put one box label on every box. Do not cover other labels.

## Sent from this plan

**FBA Shipment → Sent from this plan** lists each product line that went out with the last plan: how many units, when, and which Amazon shipment it went in. It is read-only.

![Lines sent from the last plan, ids hidden](img/fba-04-sent-from-plan.png)

## The buttons, in order (Adam or Becca only)

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

## What you should see

- After a button press, **Inbound Pending** shows a message, then clears.
- **Inbound Result** then says what happened and what to do next.
- When the labels are ready, four files appear under **Label Files**.

## Common mistakes

- **Pressing a button twice because nothing seems to happen.** Wait for **Inbound Pending** to clear.
- **Using old labels.** Always print from the shipment you are packing.
- **Wrong label size.** Use 4x6 for the thermal printer and 6-up for normal paper.
- **Pressing any button when you are not Adam or Becca.** See [Do not press](do-not-press.html).
