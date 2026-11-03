---
title: Basics
subtitle: Search, open a record, close it
slug: basics
order: 4
---

## What this chapter is for

Every page in RemBase works the same way. Learn these few things once.

## Pick a page

1. Click a page name in the menu on the left.
2. Some pages have smaller pages under them. Click the smaller page you need.

![The RemBase menu](img/start-01-menu.png)

## Find something in a list

Most pages show a list. The buttons at the top right help you find things.

![Filter, Sort and Search buttons at the top right of a list](img/basics-01-toolbar.png)

1. Click the **magnifying glass** (Search).
2. Type a part number, a name or a PO number.
3. The list now shows only matching rows.
4. To see everything again, click the **✕** in the search box.

- **Filter** hides rows you do not need. It changes only your own view.
- **Sort** changes the order of the rows. It changes only your own view.

## Open a record

1. Click a row in the list. In some lists, point at the row and click the **expand** button (two small arrows).
2. The record opens on the right side or in the middle.

On the **Home** pages (Home, Listings, Reports), you can also click a **number tile**. It opens the list of records behind the number, and each of those opens too. Most record pages are read-only. Where you can write something, the page shows a box for it (for example **Your check** or **Your plan**).

## Move between records and close

![Arrows and close button at the top of an open record](img/basics-02-panel.png)

- **A** – the arrows go to the previous or next record in the list.
- **B** – the **✕** closes the record.

## White boxes and grey text

- A **white box** with a border is a field you can type in.
- **Grey text** or text with no box is read-only. The system fills it in.
- RemBase saves what you type by itself. There is no Save button. Click outside the box or press **Tab** when you finish.

## Undo, history and comments

- Made a mistake while typing? Press **Cmd+Z** (**Ctrl+Z** on Windows) right away to undo it.
- Stock changes are always recorded in the **Ledger**: who entered them and when (receipts, counts, builds, reversals, shipments).
- On a PO line, **Price/Qty changed by / at** shows who last changed the price or quantity.
- For anything else, ask Adam. He can see the full history.
- Comments on a record are visible to everyone.

## How to scan

**RemBase Scan** is a page for your phone. It shows what RemBase knows about an item or a bin. Ask Adam for the **RemBase Scan** bookmark. You sign in with your work Google account.

1. Open the **RemBase Scan** bookmark.
2. Scan a code in one of three ways:
   - Pull the trigger on the Bluetooth scanner. You do not need to tap anything first.
   - Tap **Type**. Type the first 2 letters or numbers of the code. A list shows. Tap the right one. It works like a scan. You can also type part of the name. (TEST-BIN's code is **#9001#**.)
   - Tap **Scan with camera**.

   When you count a bin, the list shows the items RemBase expects in that bin first. When you receive, it shows only the items on that PO.
3. Read the result:
   - **An item** shows its bins and how many are in each, its lots and expiration dates, and its open POs. A date in **red** expires in less than 90 days.
   - **A bin** shows what is in it.
4. Use the buttons:
   - **Open in Inventory** opens the part in RemBase.
   - **Receive: PO …** opens that PO line, so you can receive it.
   - **Count in** a bin, or **Count this bin**, opens a count of that bin.

::: warn
**Count real bins here now.** A count on a **real** bin saves. The page says **Counts in this bin save in RemBase and go to Fishbowl automatically (within 5 min).** You do **not** count that bin again in Fishbowl.
:::

**Count a bin (phone):**

1. Scan the bin. Tap **Count this bin**. (To practice, use **TEST-BIN**.)
2. Scan each item. Each scan adds 1.
3. The phone may ask **which expiry?** Choose the expiration date printed on the item. Not sure? Tap **Not sure**. That item is not saved. Count it again.
4. If a line is right, tap **Matches**. To type a number, tap the line.
5. Tap **Finish**. You see the differences.
6. Tap **Save count to RemBase** and answer the question.
   - **Real bin:** it says **Saved. Sent to Fishbowl automatically (within 5 min).** Keep RemBase Scan open (you can count the next bin). A few minutes later you see **In Fishbowl ✓**.
   - **TEST-BIN:** it says **Saved – posting**. RemBase posts the stock changes next.

**Messages you may see:**

| Message | What to do |
|---|---|
| **Not saved: stock moved while you counted** | Count the bin again. |
| **Recount needed – not saved** | Count again, and choose the expiration date. |
| **Not confirmed – tell Adam. Code …** | Give Adam the code. |
| **No connection… kept on this phone** | Wait. It sends again by itself. |
| **Keep this page open: this phone cannot store the count.** | Keep the page open until it is saved. |
| **Sign in again…** | Sign in. The count waits for you. |

**After a real count, a red box may show at the top.** It names the bin. It stays until you tap **OK**.

| Red box | What to do |
|---|---|
| **Held for a person: big change. Becca/Adam will check it.** | Tap **OK**. Becca or Adam checks it. Do not change it in Fishbowl. |
| **Not sent to Fishbowl: this lot is not set up in Fishbowl. Adam sees it in Flags.** | Tap **OK**. Adam fixes it. Do not change it in Fishbowl. |
| **Not changed in Fishbowl: the stock changed there too. Adam sees it in Flags.** | Tap **OK**. Adam fixes it. Do not change it in Fishbowl. |

### Receive a delivery with RemBase Scan

::: warn
**Practice only for now.** Use your own practice PO and your TEST parts. On a real part the phone says **Practice only: real receipts go in Fishbowl until Adam turns on floor receipts.** Receive real deliveries in Fishbowl until Adam tells you Scan receiving is on.
:::

1. Tap **Receive a delivery**.
2. Scan the PO number on the packing slip, or tap the PO.
3. Scan each item, or tap its line.
4. Type how many. Pick the expiry date if the item has one. Scan the bin label.
5. Tap **Save receipt**. A TEST part says **Saved ✓**. RemBase posts it.
6. The same item with another date: after you save, tap **Same item, another date**.
7. An item that is **not on the PO**: the phone asks. Tap **Report an extra (tells Becca)**. Type how many, scan the bin (the hold shelf is fine) and tap **Send to Becca**. Nothing is received in RemBase. Becca adds it.
8. When the delivery is done: tap **Done with this delivery (tell Becca)**. The phone shows what is still due. Tap **Yes, tell Becca**.

**No Wi-Fi?** The phone keeps your receipt and sends it when Wi-Fi is back. If it says **Sent. RemBase has not confirmed it yet. Do NOT receive it again**, do **not** receive it again. Check the PO in a minute.

## Common mistakes

- **Typing in the wrong record.** Check the title at the top before you type.
- **Typing on a real part.** Before December 1, type only on TEST items.
- **Thinking a filter is gone.** A number next to **Filter** or **Sort** means one is on. Click it to remove it.
