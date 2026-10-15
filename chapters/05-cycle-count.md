---
title: Cycle Count
subtitle: Count the stock in a bin
slug: cycle-count
order: 5
---

## What this page is for

A **cycle count** means you count what is really in one bin and compare it with RemBase.

**Who uses it:** Chad and Sabith.

::: warn
**Counting is turned off until December 1.**

When you press **Start Count Session** now, RemBase makes an empty session with no lines. This is on purpose. Before December 1, do real counts in **Fishbowl**.

You can still open the pages and read this chapter, so you are ready.
:::

## Sub-pages

| Sub-page | What it is for |
|---|---|
| **Cycle Count** | All bins. Open a bin to count it. |
| **Count by Part** | All parts with their warehouse stock. Read-only. |

## Task: start a count

1. Click **Cycle Count** in the menu.
2. Type the bin name in **Search** (1). For practice: **TEST-BIN**.
3. Click the bin in the list.
4. Scroll down to **Count Sessions**. Click **Start Count Session** (2).

   ![Bin page with the Start Count Session button](img/cc-01-bin.png)

5. A form opens. **Counted By** shows your name (A). Click **Create** (3).

   ![Start count form](img/cc-02-start.png)

6. The new session appears under **Count Sessions**. Click it.

![Count session with no lines yet](img/cc-03-session.png)

## Task: enter your count (after December 1)

From December 1, RemBase makes one **count line** (4) for each part and lot in the bin.

1. Open the session.
2. Click each line under **Count Lines**.
3. Count that part in the bin.
4. Type the number you counted in **Actual Qty**.
5. Do this for **every** line.
6. When every line has a number, set the session **Status** to **Completed**.

::: warn
**Never leave a line empty.** An empty line counts as zero, and RemBase removes that stock.
:::

- If you find a part that has no line, do not use **Add found item**. Write it down and tell Becca.

## What you should see

- The session status is **Completed**.
- The bin shows a new **Last Counted Date**.
- If your count was different, RemBase fixes the stock and makes a **Flag** for Becca.

## Count by Part

![Count by Part list](img/cc-04-by-part.png)

This list shows each part and its warehouse stock. Use it to check a number. It is read-only.

## Common mistakes

- **Counting the wrong bin.** Check the bin name at the top before you count.
- **Leaving a line empty.** Empty = zero.
- **Counting cases instead of units.** Count single units.
- **Starting two sessions for one bin.** Look at **Count Sessions** first.
