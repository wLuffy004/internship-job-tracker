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


---
## 2026-06-28

### Problem 217: Contains Duplicate

**Difficulty:** Easy  
**Topics:** Array, Hash Table, Set  
**Status:** Accepted  

**Core Idea:**  
Use a set called `seen` to store the numbers that have already appeared.  
For each number in `nums`, check whether the number is already in `seen`.  
If the number is already in `seen`, return `True` because a duplicate exists.  
Otherwise, add the current number to `seen`.  
If the loop finishes without finding any duplicate, return `False`.

**Time Complexity:** O(n)  
The algorithm only loops through the array once.

**Space Complexity:** O(n)  
In the worst case, the set may store up to n numbers.

**Did I solve it independently?**  
Completed with guidance.

**What I learned:**  
I learned the difference between a dictionary and a set.  
A dictionary stores key-value pairs, while a set only stores unique values.  
For this problem, a set is cleaner because I only need to check whether a number has appeared before.  
I also learned that `return False` should be outside the for loop, because the whole array must be checked first.
