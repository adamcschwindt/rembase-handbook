---
title: "Becca: quick start"
subtitle: Six short tasks to learn RemBase
slug: becca-try-it
order: 1
---

## Read this first

- **Until December 1, real work stays in Fishbowl.** In RemBase you only look, or you practice on TEST items.
- **Your practice items:** first PO **TEST-PRACTICE-BECCA** (finish it in Task 4), new PO **TEST-PRACTICE-BECCA-2** with your parts **TEST-BECCA-A** (#9111#) and **TEST-BECCA-B** (#9112#), bin **TEST-BIN** (#9001#).
- **RemBase saves by itself.** There is no Save button. Press **Tab** or click outside the box.
- **Never delete anything.** If something gets deleted by mistake, tell Adam. Nothing else is needed.
- **Made a typing mistake?** Press **Cmd+Z** (**Ctrl+Z** on Windows) right away to undo it.
- **While you practice, never press these buttons:**
  - **Email PO**
  - **Email Staged POs**
  - **Delete Staged POs**
  - **Create "…"** in a part list
  - **Escalate To Asana**
  - Anything on the **Ads** page
  - The Amazon buttons on **FBA Shipment**
  - The label buttons on **CC Orders**
- Everything else in these steps is safe. You do not have to worry about breaking anything.

**When:** Task 1 every morning. Task 2 when you plan an order. Task 3 once a month. Do the practice tasks in this order: 4 → 5 → 6.

## Task 1 – Morning check on Home (look only)

**Goal:** see today's sales and our Amazon storage space.

1. In the RemBase menu, click **Home**, then **Home**.
   - Sign in with your **work** Airtable account if it asks.
2. Look at the first box, **Today so far**.
   - This is today's Amazon sales, so far. It updates every hour.
   - It is not the full day. **D – Note** says how much is an estimate.
3. Scroll down to **Sales (Amazon.com)**. Look at **Last full day sales**.
   - This is yesterday's final number.
4. Scroll down to **FBA storage space**. Look at **E – Level**.
   - **OK** (green) = fine.
   - **Watch** (yellow) = 85% of our limit or more.
   - **Over** (red) = 100% of our limit or more. If you see red, tell Adam.

**Done when:** you have looked at all three parts.

More help: [Home](home.html).

## Task 2 – See what to order on PO Planning (look only)

**Goal:** see what RemBase says we should order. Until December 1, you still make the real PO in **Fishbowl**.

1. In the RemBase menu, click **Purchase Orders**, then **PO Planning**.
   - The parts with the biggest **Recommended Order Qty** are at the top.
2. To find one part, click **Search** (the magnifying glass) and type the SKU or the product name.
3. Read **Recommended Order Qty**. This is how many RemBase says we should order.
   - It covers the next **90 days** of sales, adjusted for the season.
   - For a part that goes into packs, the packs' sales count too (**Demand from packs (90d)**).
4. Scroll right. Check what we already have:
   - **Open PO Qty** = already ordered, not received yet.
   - **Warehouse On Hand Qty** = in our warehouse.
   - **FBA On Hand Qty** and **FBA Inbound Qty** = at Amazon, and on the way to Amazon.
5. Make the real PO in **Fishbowl**, like before.
6. Do not tick **Start New PO For Vendor** or **Planning Add To PO**. Do not press **Commit / Clear**.
7. Does a number look wrong? Tell Adam the SKU and the number you expected. Adam fixes RemBase.

**Done when:** you have checked the parts you want to order.

More help: [PO Planning](purchase-orders.html#po-planning-look-only).

## Task 3 – Once a month: check aged stock on Home (look only)

**Goal:** see which of our units at Amazon are getting old (181 days or more).

1. In the RemBase menu, click **Home**, then **Home**.
2. Scroll down to **Aged FBA stock (181+ days)**.
   - The big number = all our units at Amazon that are 181 days old or more.
3. Look at the list under it, **Aged stock by brand**.
   - Each brand has a group. The grey header line shows that brand's totals.
   - Columns:
     - **Units 181-270 / 271-365 / 365+** = how old.
     - **Est. Surcharge** = Amazon's estimated aged-stock fee.
     - **Est. Storage Next Month** = next month's storage cost.
     - **Sell-through** = how fast it sells.
     - **Recommended Action** and **Recommended Sale Price** = Amazon's advice. Blank = Amazon gave none.
4. Look at the **Snapshot Date** column.
   - This is the day Amazon counted the ages, usually a few days before today.
5. Optional: open a product in the list (point at the row and click the **expand** button). In **Your plan**, choose a **Plan** and add a **Plan Note**. You cannot change the numbers.

**Done when:** you have looked at every brand group.

More help: [Home → Aged FBA stock](home.html#aged-fba-stock).

## Task 4 – Practice: finish your first PO, then receive your new PO (TEST only)

**Goal:** finish your first practice PO, then receive your new one.

::: warn
**Always pick the bin.** If a receipt has no bin, nothing is added to stock, and a flag appears within about an hour.

**Already saved a receipt with no bin?** Do **not** receive again. Open the receipt: **Receiving** → your PO line → **Received so far** → click the receipt with no bin. In the box **Add the bin (receipt not posted yet)**, type or scan the bin barcode and press **Enter**. For practice, TEST-BIN's barcode is **#9001#**. It posts once.
:::

Pick the line by product name (**TEST component A** or **TEST component B**), not by number.

If a line already says **Fulfilled**, you already received it. Go to the next line.

**Part 1 – Finish your first PO (TEST-PRACTICE-BECCA)**

| Product | Ordered | Received | Still open |
|---|---|---|---|
| **TEST component B** (TEST-COMP-B) | 24 | 0 | 24 |
| **TEST component A** (TEST-COMP-A) | 24 | 1 | 23 |

Your first PO also has an empty line you started (…-L3). You can type **10** in its **Qty Ordered**, or leave it.

*TEST component B: receive all 24*

TEST component B shows **24** still to receive. That is correct. If you already saved a receipt there without a bin, add the bin (see the box above) instead of receiving again.

1. In the RemBase menu, click **Receiving**.
2. Click **Search** at the top of the list and type **TEST-PRACTICE-BECCA**.
3. Click the row for **TEST component B**.
4. Look at **Received so far**.
   - This check stops you from receiving twice.
5. Click **Receive**. The **Receive Shipment** form opens.

   ![Receive Shipment form with Bin Scan and Bin (Actual) marked](img/rcv-03-form.png)

6. **4 – Received By:** choose **Becca**.
7. **5 – Quantity Received (Units):** type **24**. Leave **Cases** empty.
8. **6 – Expiration Date:** type **12/31/2027**.
9. **7 – Bin Scan:** scan the bin barcode (TEST-BIN = **#9001#**). No scanner? Type **#9001#**.
10. Check every box again.
11. Click **8 – Post Receipt**.
    - You should see the receipt under **Received so far**.
    - **Derived Status** = **Fulfilled**, and **Outstanding Qty** = 0.
    - The line leaves the Receiving list. That is correct.

*TEST component A: receive part, then close it short*

12. Back on **Receiving**, search **TEST-PRACTICE-BECCA** again.
13. Click the row for **TEST component A**.
14. Look at **Received so far**. It already shows **1** unit, from a test on 10/19.
15. Click **Receive**.
16. **Received By:** **Becca**.
17. **Quantity Received (Units):** **20**.
18. **Expiration Date:** **12/31/2027**.
19. **Bin Scan:** scan the bin barcode (TEST-BIN = **#9001#**).
20. Click **Post Receipt**.
    - You should see **Derived Status** = **Partial** and **Outstanding Qty** = **3**.
21. Pretend the vendor confirmed that the last 3 are not coming. (In real work, Chad checks with the vendor, then Vicky ticks this box. You are the backup.)
    - In the **Quantities** group, tick **B – Close this line short (rest is not coming)**.

      ![PO line with Line Type and the Close this line short box marked](img/rcv-09-short.png)

    - You should see **Derived Status** = **Closed Short** and **Outstanding Qty** = 0. The line leaves the list.

**Part 2 – More practice: receive TEST-PRACTICE-BECCA-2**

22. Search **TEST-PRACTICE-BECCA-2** on **Receiving**.
23. Receive **TEST-BECCA-A** and **TEST-BECCA-B** (24 each) the same way. Bin: scan **#9001#** (TEST-BIN).

If you make a mistake, you may press **Reverse this receipt**, then receive again. See [Fix a wrong receipt](receiving.html#fix-a-wrong-receipt).

**Done when:** all lines of both POs have left the Receiving list.

More help: [Receiving](receiving.html).

## Task 5 – Practice: close a TEST flag (TEST only)

**Goal:** read a flag and mark it done.

1. In the RemBase menu, click **Flags**, then **All Open Flags**.
   - Do not use **My Open Flags**. It looks empty, because flags are not assigned to people yet.
2. Search **TEST-PRACTICE-BECCA**.
3. Click the flag **Receipt reversed: TEST-PRACTICE-BECCA-L2**.
4. Read the title and the **Note**.
   - The note says to receive the line again with the right numbers. You did that in Task 4.
5. Set **Status** to **Resolved**.
   - The flag leaves the open list.
6. If Task 4 made any new flag with **TEST** in the title, open it, read it and set it to **Resolved** too.
7. **Do not** tick **Escalate To Asana**. It makes a real Asana task.
8. Leave every real flag alone (no TEST in the title).
   - Before December 1, real problems are fixed in Fishbowl.

**Done when:** no open flag for TEST-PRACTICE-BECCA is left.

## Task 6 – Practice: add a line to a PO and open the PO PDF (TEST only)

**Goal:** add one line to your new practice PO (TEST-PRACTICE-BECCA-2) and see the PDF update.

1. In the RemBase menu, click **Purchase Orders**.
2. Search **TEST-PRACTICE-BECCA-2** and click the PO number.
   - Only open PO numbers that start with **TEST-** or **PRACTICE-**. Real POs look like 2026-061.
3. In **PO Lines**, click the **+** under the last line.
   - A new empty line appears.
4. Click the **+** in the new line's **Part** cell.
5. Type **TEST-BECCA-A** and click it in the list.
   - Never click **Create "…"** at the bottom of the list.
6. Point at the new line and click the **expand** button (two small arrows).

   ![Expand button to open a PO line](img/po-05-expand-line.png)

7. **Qty Ordered:** type **10**.
8. **Unit Cost:** type **1.00**.
   - If you leave Unit Cost empty, RemBase fills the last price paid and shows **Check it**.
9. Press **Tab**. RemBase saves by itself.
10. Close the line (the **✕** at the top).
    - You should see the new line in **PO Lines**.
11. Wait a few minutes. Then click the file under **PO PDF**.
    - The PDF now shows your new line. RemBase makes the PDF by itself.
12. Do not change **Status**. It changes by itself (Issued / Partial / Fulfilled).
13. **Do not** press **Email PO**.
14. Extra practice (optional): your new line now shows on **Receiving**. You can receive it as in Task 4 (10 units, bin **#9001#**).

**Done when:** your new line shows in the PO PDF.

More help: [Purchase Orders](purchase-orders.html).

## Not in these steps (and why)

- **Ticks on PO Planning and Run Planning, and New Part:** these are shared with real planning. There is nothing safe to practice before December 1. You can look at them.
- **Listing alerts (Home → Listings):** Karly's task. See [Karly: quick start](karly-quick-start.html).
- **Cycle count, production runs, Next shipment:** floor jobs (Chad and Sabith).
- **Claims:** Karly's weekly task.
- **Ads:** on hold.
