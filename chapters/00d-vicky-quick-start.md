---
title: "Vicky: quick start"
subtitle: Four short tasks for costs and short lines (look only)
slug: vicky-quick-start
order: 3
---

## Read this first

- **Receiving is real in RemBase now.** Here you check PO costs and close damaged receipts. Bills and payments stay in QuickBooks.
- **RemBase saves by itself.** There is no Save button.
- **Made a typing mistake?** Press **Cmd+Z** (**Ctrl+Z** on Windows) right away to undo it.
- **Never press** **Email PO**. See [Do not press](do-not-press.html).

## Task 1 – Read the costs on a PO (look only)

**Goal:** see the price of each line on a PO.

1. In the RemBase menu, click **Purchase Orders**.
2. Click **Search** and type the PO number. Click the PO number.
3. Under **PO Lines**, point at a line and click the **expand** button (two small arrows).
4. Read **Unit Cost** (the price for one unit) and **Qty Ordered**.
5. **Cost from last paid. Check it.** means RemBase filled in the last price we paid. Check it against the vendor's bill.
6. **Price/Qty changed by** and **Price/Qty changed at** show who last changed the price or the quantity, and when.

**Done when:** you have read the costs on one PO.

More help: [Purchase Orders](purchase-orders.html).

## Task 2 – Before you pay a vendor bill: check the PO Variance Report (look only)

**Goal:** see if what arrived matches what we ordered.

1. In the RemBase menu, click **Purchase Orders**, then **PO Variance Report**.
2. Click **Search** and type the PO number.
3. Read **Discrepancy Flag** on each line:
   - **Short** = less arrived than we ordered.
   - **Over** = more arrived than we ordered.
   - **Damage** = some arrived damaged.
4. Read **Discrepancy Notes**. It says what is wrong.
5. Compare with the vendor's bill.

Real deliveries are received in RemBase now (since November 4), so real lines show here.

**Done when:** you have checked the lines of the PO on the bill.

More help: [Purchase Orders](purchase-orders.html).

## Task 3 – Close a line short

**Goal:** close a PO line when the rest is not coming.

Chad checks with the vendor first. Then you close the line.

1. In the RemBase menu, click **Receiving**. Search the PO number. Click the line.
2. In the **Quantities** group, find the box **B – Close this line short (rest is not coming)**.
3. When Chad confirms that the rest is not coming, you tick it. **Derived Status** changes to **Closed Short**.

For now, look only. Do not tick it on a real line before December 1. A practice PO for you is coming.

More help: [Wrong amounts on a PO](receiving.html#wrong-amounts-on-a-po).

## Task 4 – Something arrived that was not ordered, or too many

- **Not on the PO:** before December 1, Becca adds the line in Fishbowl with the vendor's price.
- **More than ordered:** RemBase makes a flag for Becca. If the extra units cost nothing, no approval is needed.

More help: [Wrong amounts on a PO](receiving.html#wrong-amounts-on-a-po).

## Task 5 – Close a damaged receipt

**Goal:** tell RemBase if the vendor gave a credit for damaged units.

When the floor receives damaged units, they go to the **DAMAGED** bin, and you get an Asana task.

1. Ask the vendor for a credit.
2. Open the link in your Asana task. The flag opens.
3. At the bottom, choose **Damaged Outcome**:
   - **Credit received** – the vendor credits the damaged units.
   - **No credit - scrap** – we write them off.
4. **Credit Reference:** type the credit memo number (you may leave it empty).
5. **Credited Units:** how many units the vendor credited. Leave it empty if the vendor credited all of them. The rest are written off.
6. RemBase does the rest. Read **Damaged Close Result**: it says what was done, or why it is still waiting.

**Done when:** **Damaged Close Result** says what was done.

## Good to know

- **Packaging (boxes and other supplies):** these orders get a PO in RemBase. Soon RemBase makes them by itself from the vendor's order email.
- **Boxes and packaging are Inventory Asset**, with their freight. The bill never goes to COGS. A box becomes part of the product cost when it is used in a run, and COGS when the product sells.
- **QuickBooks:** from **November 7** at the earliest (Adam tells you the day), RemBase sends bills and journals to QuickBooks. Their numbers start with **RB**. Attach the vendor invoice to each bill.

## Not your job (who does it)

- **Receiving, counts, runs:** Chad and Sabith.
- **POs and planning:** Becca.
- **Something in RemBase does not work:** Adam. See [Who to ask](who-to-ask.html).
