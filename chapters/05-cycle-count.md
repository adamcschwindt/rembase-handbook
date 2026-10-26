---
title: Cycle Count
subtitle: Count the stock in a bin
slug: cycle-count
order: 7
---

## What this page is for

A **cycle count** means you count what is really in one bin and compare it with RemBase.

**Who uses it:** Chad and Sabith.

::: warn
Before December 1, do real counts in **Fishbowl**. In RemBase, practice only on **TEST-BIN**.

If you complete a count session on a **real** bin before December 1, RemBase changes **no** stock. It makes one flag ("Practice count…").
:::

A count session with status **Failed – floor app** or **Cancelled – duplicate**: never complete it. Count the bin again.

In the **Cycle Count** list, each bin shows its scan code and what is in it. You can also scan a bin with **RemBase Scan**. See [Basics](basics.html#how-to-scan).

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

## Task: enter your count

RemBase makes one **count line** (4) for each part and lot in the bin. **Expected** is what RemBase thinks is there.

![Count session with its count lines](img/cc-03-session.png)

1. Open the session.
2. Click each line under **Count Lines**.
3. Count that part in the bin.
4. Type the number you counted in **Actual Qty** (6). **Expected Qty** (A) shows what RemBase thinks is there.

   ![A count line with Expected Qty and Actual Qty](img/cc-05-actual.png)

5. Close the line (✕ at the top right). Do the same for **every** line.
6. When every line has a number, click **Status** and choose **Completed** (7).

   ![Status list with Completed](img/cc-06-complete.png)

::: warn
**Count every line.** If you leave a line empty, RemBase skips it and changes nothing, so that part is not counted at all.
:::

- If you find a part that has no line, do not use **Add found item**. Write it down and tell Chad. Chad checks first (is it in the wrong bin?). Ask Becca only if a new part must be created.

## What you should see

![Finished count session](img/cc-07-done.png)

- The session status is **Completed**, with the time it was completed.
- The bin shows a new **Last Counted Date**.
- If your count was different, RemBase makes a **Flag** for Becca and changes the stock:
  - a small difference (under the approval limit) changes the stock right away;
  - a big difference waits in **[Approvals](other-pages.html)** until Becca or Adam says yes.

## Count by Part

![Count by Part list](img/cc-04-by-part.png)

This list shows each part and its warehouse stock. Use it to check a number. It is read-only.

## Common mistakes

- **Counting the wrong bin.** Check the bin name at the top before you count.
- **Leaving a line empty.** RemBase skips it, so that part is not counted.
- **Counting cases instead of units.** Count single units.
- **Starting two sessions for one bin.** Look at **Count Sessions** first.
