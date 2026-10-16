---
title: Receiving
subtitle: Enter what arrived from a vendor
slug: receiving
order: 4
---

## What this page is for

When boxes arrive from a vendor, you **receive** them. Receiving puts the stock in a bin with its expiration date.

**Who uses it:** Chad and Sabith.

::: warn
Before December 1, receive real deliveries in **Fishbowl**. In RemBase, practice only on **your own practice PO** (TEST-PRACTICE-BECCA, -CHAD or -SABITH). The pictures use TEST-HB-1.
:::

## The Receiving page

![Receiving list with the practice lines](img/rcv-01-list.png)

1. Click **Receiving** in the menu.
2. Use **Search** to find a PO number or a part.

Each row is one PO line. Click a row to see what was ordered and what has arrived.

During practice this list shows only TEST lines. Real parts are hidden on purpose.

Until December 1, a receipt on a **real** part is blocked: the receipt line says **Blocked – not posted**, nothing is added to stock, and a Flag goes to Becca. Practice only on TEST POs.

## Task: receive a PO line

Today the **Receive** button is on the PO line page in **Purchase Orders**.

1. Click **Purchase Orders** in the menu.
2. Click the PO number (for practice: **your own practice PO**). Receive into **TEST-BIN**.
3. In **PO Lines**, point at the line. Click the **expand** button (two small arrows).
4. At the top, next to **Receipt Lines**, click **Receive**.

   ![Receive button on a PO line](img/rcv-02-receive-button.png)

5. The **Receive Shipment** form opens. Fill it in:

   ![Filled Receive Shipment form](img/rcv-03-form.png)

   - **4 – Received By:** choose your name.
   - **5 – Quantity Received (Units):** how many single units arrived. Use this for most receipts.
   - **Quantity Received (Cases):** only for full cases. Leave it empty if you typed Units.
   - **6 – Expiration Date:** the date on the box. Always fill it in if the box has a date.
   - **Quantity Damaged:** how many are broken. Leave it empty if none.
   - **Discrepancy Notes:** write what is wrong, if anything.
   - **7 – Bin (Actual):** the bin where you put the stock. It is required.

6. To choose the bin, click **+ Add record**, type the bin name, and click the bin.

   ![Bin picker with the practice bin](img/rcv-04-bin.png)

7. Check every box again.
8. Click **Post Receipt** (8).

## What you should see

The receipt appears under **Receipt Lines**. On the Receiving page, the line shows:

![Quantities and the receipt list after receiving](img/rcv-05-done.png)

- **Qty Received** goes up.
- **Outstanding Qty** goes down.
- **Derived Status** says **Partial** or **Fulfilled**.
- **Received so far** lists each receipt with the bin and the expiration date.

The stock is now on the part page in [Inventory](inventory.html).

## Open POs

**Receiving → Open POs** lists POs that are not finished. It shows how much is still outstanding. It is read-only.

![Open POs list](img/rcv-06-open-pos.png)

## Common mistakes

- **Typing cases in the Units box.** Units = single items. Cases = full cases.
- **No expiration date.** Without a date the system cannot use the oldest stock first.
- **Wrong bin.** Choose the bin where the stock really is.
- **Receiving twice.** Look at **Received so far** before you receive.
- **A wrong receipt.** Do not try to fix it yourself. Ask Becca. (**Reverse this receipt** is on the [Do not press](do-not-press.html) list.)
