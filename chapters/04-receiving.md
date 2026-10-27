---
title: Receiving
subtitle: Enter what arrived from a vendor
slug: receiving
order: 7
---

## What this page is for

When boxes arrive from a vendor, you **receive** them. Receiving puts the stock in a bin with its expiration date.

**Who uses it:** Chad and Sabith.

::: warn
Before December 1, receive real deliveries in **Fishbowl**. In RemBase, practice only on **your own practice PO** (TEST-PRACTICE-BECCA-2, -CHAD-2 or -SABITH-2). The pictures use TEST-HB-1.
:::

## The Receiving page

![Receiving list grouped by PO, with the practice lines](img/rcv-01-list.png)

1. Click **Receiving** in the menu (1).
2. Use **Search** (2) to find a PO number or a part.

The list is grouped by PO (3). Each row is one PO line, with the product name and its **Derived Status**. The list shows the lines that still have something to receive, and the lines received in the last 14 days. Click a row to see what was ordered and what has arrived.

A PO line number (like TEST-HB-1-L1) never changes once it is made.

On the line page:

- **Outstanding Qty** = how many are still to come.
- **Receipt status** warns you when a receipt on this line is not posted.
- **Case math** warns you when the part has no **Units Per Case**. Then receive in **Units**.

**Cost from last paid. Check it.** means the Unit Cost was filled in from the last price paid. **Price/Qty changed by / at** shows who last changed the price or quantity, and when. See [Purchase Orders](purchase-orders.html).

During practice this list shows only TEST lines. Real parts are hidden on purpose.

Until December 1, a receipt on a **real** part is blocked: its **Post Status** says **Blocked (Fishbowl is stock master)**, nothing is added to stock, and a flag is made. Practice only on TEST POs.

::: warn
**Always pick the bin.** If a receipt has no bin, nothing is added to stock. Its **Post Status** says **Not posted – needs bin**. See [Forgot the bin](#forgot-the-bin).
:::

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
     - You can still fix the date on the receipt before it is posted.
     - One receipt has one expiration date. If the boxes have two different dates, make two receipts: one for each date.
   - **Quantity Damaged:** how many are broken. Leave it empty if none.
   - **Discrepancy Notes:** write what is wrong, if anything.
   - **7 – Bin Scan** or **Bin (Actual):** the bin where you put the stock. You must fill in one of them. For practice: **TEST-BIN**.
     - **Bin Scan:** scan the bin label, or type the bin name. For practice: scan **#9001#** or type **TEST-BIN**.
     - **Bin (Actual):** or choose the bin from the list.

2. To choose the bin from the list, click **+ Add record** under **Bin (Actual)**, type the bin name, and click the bin.

   ![Bin picker with the practice bin](img/rcv-04-bin.png)

3. Check every box again.
4. Click **Post Receipt** (8).

## What you should see

The receipt appears under **Received so far** (and under **Receipt Lines** on the PO line):

![Quantities, Receipt status and Case math on a received line, and the receipt list](img/rcv-05-done.png)

- **Qty Received** goes up.
- **Outstanding Qty** goes down.
- **Derived Status** says **Partial** or **Fulfilled**.
- **Received so far** lists each receipt with the bin, the expiration date, who received it, **Received At** (Eastern time) and **Post Status**.

**Post Status** on each receipt:

| Post Status | What it means |
|---|---|
| **Posted** | The stock is in the bin. |
| **Not posted – needs bin** | No bin yet. [Add the bin](#forgot-the-bin). |
| **Not posted – problem** | **Post problem** on the receipt says what is wrong, for example "Bin 'X' not found. Scan the bin label again, or type the bin name". |
| **Cancelled (not posted)** | Cancelled before it was posted. No stock changed. |
| **Reversed** | It was posted, then taken back out. |
| **⚠ Expiry changed after posting: reverse and receive again** | Someone changed the date after posting. Reverse it and receive again. |
| **Blocked (Fishbowl is stock master)** | A real part before December 1. Nothing posted. |
| **Historical** | An old receipt copied from Fishbowl. |

**Entry warning** on a receipt is a warning only. The receipt is still accepted. For example: the expiration date is soon, or the part has no **Units Per Case** (receive in **Units**, or ask Becca to set Units Per Case).

The stock is now on the part page in [Inventory](inventory.html).

## Open POs

**Receiving → Open POs** lists POs that are not finished, with how much is still outstanding. Click a PO to open it, then receive a line as in Way 2.

![Open POs list](img/rcv-06-open-pos.png)

## Forgot the bin

Already saved a receipt with no bin, or with a wrong bin? Its **Post Status** says **Not posted**. **Do not receive again.**

1. Open the receipt: **Receiving** → your PO line → **Received so far** → click the receipt.
2. In the box **Add the bin (receipt not posted yet)**, scan the bin label or type the bin name, and press **Enter**. For practice: **#9001#** or **TEST-BIN**.
3. The receipt posts once.

## Fix a wrong receipt

Anyone in the warehouse may press **Reverse or cancel this receipt**.

- A receipt that is **not posted** yet is **cancelled**. No stock changes.
- A receipt that is **posted** is **reversed**. The stock is taken back out.

1. Open the receipt: **Receiving** → the PO line → **Received so far** → click the receipt.
2. In **Reverse Reason**, type why. You must write a reason.
3. Press **Reverse or cancel this receipt** and confirm.
4. Read **Reverse Result**. **OK** means it worked.
5. Receive the line again with the right numbers. A new receipt is made (…-R2).

Wrong expiration date? Before the receipt is posted, just fix the date on the receipt. After it is posted, reverse it and receive again.

If **Reverse Result** says:

| Message | What it means |
|---|---|
| **REFUSED: type why in the Reverse Reason box first** | Write a reason, then press the button again. |
| **REFUSED … Ask a manager** | The stock was already used or moved. Nothing changed. Tell Becca or Chad. |
| **REFUSED … came from Fishbowl** | Until December 1, fix it in Fishbowl. |
| **REFUSED: this receipt was already cancelled** or **already reversed** | Nothing to do. |

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
- The rest is **not** coming: Chad checks with the vendor that the rest is not coming. Then Vicky opens the line on the **Receiving** page and ticks **B – Close this line short (rest is not coming)**. Becca is the backup.

## Common mistakes

- **Typing cases in the Units box.** Units = single items. Cases = full cases.
- **No expiration date.** Without a date the system cannot use the oldest stock first.
- **Two expiration dates on one receipt.** Make one receipt for each date.
- **Wrong bin.** Choose the bin where the stock really is.
- **Receiving an item on the wrong line.** If it is not on the PO, ask Becca to add a Not Ordered line first.
- **No bin, or a bin that is not found.** The receipt is **not** posted. Do not receive again. [Add the bin](#forgot-the-bin). Then it posts once.
- **Receiving twice.** Look at **Received so far** before you receive.
- **Saving a receipt with no quantity.** It is not posted. Cancel it (see [Fix a wrong receipt](#fix-a-wrong-receipt)), then receive again with the right quantity.
- **A wrong receipt.** Write a **Reverse Reason**, press **Reverse or cancel this receipt**, then receive again. See [Fix a wrong receipt](#fix-a-wrong-receipt).
