---
title: Receiving
subtitle: Enter what arrived from a vendor
slug: receiving
order: 5
---

## What this page is for

When boxes arrive from a vendor, you **receive** them. Receiving puts the stock in a bin with its expiration date.

**Who uses it:** Chad and Sabith.

::: warn
Before December 1, receive real deliveries in **Fishbowl**. In RemBase, practice only on **your own practice PO** (TEST-PRACTICE-BECCA, -CHAD or -SABITH). The pictures use TEST-HB-1.
:::

## The Receiving page

![Receiving list with the practice lines](img/rcv-01-list.png)

1. Click **Receiving** in the menu (1).
2. Use **Search** (2) to find a PO number or a part.

Each row is one PO line that still has something to receive. Click a row to see what was ordered and what has arrived. When everything on a line has arrived, the line leaves this list. Each row also shows the product's scan keys (the codes you can scan).

During practice this list shows only TEST lines. Real parts are hidden on purpose.

Until December 1, a receipt on a **real** part is blocked: the receipt line says **Blocked – not posted**, nothing is added to stock, and a Flag goes to Becca. Practice only on TEST POs.

## Task: receive a PO line

There are three ways to open the **Receive** form. All three open the same form. Way 1 is the easiest.

**Way 1 – from the Receiving page**

1. Click **Receiving** in the menu. Click your line (for practice: **your own practice PO**).
2. Scroll down to **Received so far**. Click **Receive** (3).

   ![Receive button on the Receiving page](img/rcv-02-receive-button.png)

**Way 2 – from Purchase Orders**

1. Click **Purchase Orders** in the menu. Click the PO number.
2. In **PO Lines**, point at the line. Click the small **expand icon (⤢)** at the left of the row. A plain click on the row only selects a box, it does not open the line.

   ![The expand icon at the left of a PO line](img/rcv-08-expand.png)

3. Next to **Receipt Lines**, click **Receive** (3).

   ![Receive button on a PO line](img/rcv-07-po-receive.png)

**Way 3 – from Open POs**

1. Click **Receiving → Open POs**. Click the PO.
2. Then do Way 2, step 2 and step 3: point at the line, click **⤢**, then click **Receive**.

**Then fill in the Receive Shipment form**

1. Fill in the boxes:

   ![Receive Shipment form with Bin Scan and Bin (Actual) marked](img/rcv-03-form.png)

   - **4 – Received By:** choose your name.
   - **5 – Quantity Received (Units):** how many single units arrived. Use this for most receipts.
   - **Quantity Received (Cases):** only for full cases. Leave it empty if you typed Units.
   - **6 – Expiration Date:** the date on the box. Always fill it in if the box has a date.
   - **Quantity Damaged:** how many are broken. Leave it empty if none.
   - **Discrepancy Notes:** write what is wrong, if anything.
   - **7 – Bin Scan** or **Bin (Actual):** the bin where you put the stock. You must fill in one of them. For practice: **TEST-BIN**.
     - **Bin Scan:** scan the bin label into this box.
     - **Bin (Actual):** or choose the bin from the list.

2. To choose the bin from the list, click **+ Add record** under **Bin (Actual)**, type the bin name, and click the bin.

   ![Bin picker with the practice bin](img/rcv-04-bin.png)

3. Check every box again.
4. Click **Post Receipt** (8).

## What you should see

The receipt appears under **Received so far** (and under **Receipt Lines** on the PO line):

![Quantities and the receipt list after receiving](img/rcv-05-done.png)

- **Qty Received** goes up.
- **Outstanding Qty** goes down.
- **Derived Status** says **Partial** or **Fulfilled**.
- **Received so far** lists each receipt with the bin, the expiration date, who received it, and **Received At**: the date and time in Eastern time.

The stock is now on the part page in [Inventory](inventory.html).

## Open POs

**Receiving → Open POs** lists POs that are not finished, with how much is still outstanding. Click a PO to open it, then receive a line as in Way 2.

![Open POs list](img/rcv-06-open-pos.png)

## Wrong amounts on a PO

![PO line with Line Type and the Close this line short box marked](img/rcv-09-short.png)

**Something arrived that is not on the PO (Not Ordered)**

- Before December 1, Becca first adds the line in **Fishbowl**, with the price from the vendor. Then it is received as normal.
- In RemBase the line shows **A – Line Type: Not Ordered**.
- Never receive it on the line of another product.

**More arrived than we ordered (Over)**

- Receive what arrived.
- RemBase makes a flag for Becca about the extra units.
- If the extra units cost nothing, no approval is needed.

**Less arrived than we ordered (Short)**

- The rest is still coming: leave the line open.
- The rest is **not** coming: Becca opens the line on the **Receiving** page and ticks **B – Close this line short (rest is not coming)**. Only Becca does this.

## Common mistakes

- **Typing cases in the Units box.** Units = single items. Cases = full cases.
- **No expiration date.** Without a date the system cannot use the oldest stock first.
- **Wrong bin.** Choose the bin where the stock really is.
- **Receiving an item on the wrong line.** If it is not on the PO, ask Becca to add a Not Ordered line first.
- **No bin, or a bin scan that does not match one bin.** The receipt is **not** posted, and a flag is made. Fix the bin. Then it posts once.
- **Receiving twice.** Look at **Received so far** before you receive.
- **Saving a receipt with no quantity.** RemBase raises a flag. Enter the receipt again with the right quantity.
- **A wrong receipt.** Do not try to fix it yourself. Ask Becca. (**Reverse this receipt** is on the [Do not press](do-not-press.html) list.)
