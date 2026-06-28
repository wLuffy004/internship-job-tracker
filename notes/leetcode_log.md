## 2026-06-27

### Problem 1: Two Sum

**Difficulty:** Easy
**Topics:** Array, Hash Table
**Status:** Accepted

**Core Idea:**
Use a hash map called `seen` to store the numbers that have already appeared and their indices.
For each number in `nums`, calculate `need = target - num`.
If `need` is already in `seen`, return the index of `need` and the current index.
Otherwise, store the current number and its index in `seen`.

**Time Complexity:** O(n)
The algorithm only loops through the array once.

**Space Complexity:** O(n)
In the worst case, the hash map may store up to n numbers.

**Did I solve it independently?**
Completed with guidance.

**What I learned:**
I learned how to use a dictionary/hash map to reduce the time complexity from O(n²) to O(n).
I also learned that `enumerate(nums)` gives both the index and the value while looping through a list.
