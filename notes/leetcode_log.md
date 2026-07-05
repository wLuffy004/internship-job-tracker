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

## 2026-07-01
### LeetCode 242 - Valid Anagram

Topic:
- Hash Table
- Frequency Count

Key Idea:
Use a dictionary to count characters in one string, then subtract character counts using the other string.

What I learned:
- `dict.get(key, 0)` returns the current value if the key exists
- If the key does not exist, it returns the default value `0`
- Frequency count problems often use `dict[key] = dict.get(key, 0) + 1`

Time Complexity:
- O(n)

Space Complexity:
- O(1) if only lowercase English letters are used
- O(k) for a general character set

### LeetCode 383 - Ransom Note

Topic:
- Hash Table
- Frequency Count

Key Idea:
Use a dictionary to count available characters from magazine, then use ransomNote to consume those characters.

What I learned:
- If characters cannot be reused, use a dictionary to track counts
- If characters can be reused, a set is enough to check existence
- `char_count[char] -= 1` means one available character has been used
- If the count becomes negative, there are not enough characters

Time Complexity:
- O(n + m)

Space Complexity:
- O(k)

## 2026-07-04
### LeetCode 49 - Group Anagrams

Topic:
- Hash Table
- Dictionary
- Sorting

Key Idea:
Use a dictionary to group words by their sorted character sequence.  
Words that are anagrams will have the same sorted result.

What I learned:
- Use a dictionary when grouping data by key
- Use a set when only checking existence or duplicates
- Lists use `append()`, while sets use `add()`
- `sorted(word)` returns a sorted list of characters
- `"".join(sorted(word))` converts the sorted character list back into a string
- Words with the same sorted result belong to the same anagram group
- `list(groups.values())` returns all grouped word lists

Important Example:
```python
word = "eat"
key = "".join(sorted(word))
```

Result:
```python
sorted("eat")
# ['a', 'e', 't']

"".join(['a', 'e', 't'])
# "aet"
```

Grouping Example:
```python
{
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"],
    "abt": ["bat"]
}
```

Time Complexity:
- O(n * k log k)

Space Complexity:
- O(n * k)

## 2026-07-05
### LeetCode 347 - Top K Frequent Elements

Topic:
- Hash Table
- Dictionary
- Sorting
- Lambda
- List Slicing

Key Idea:
Count the frequency of each number using a dictionary, sort the dictionary by frequency in descending order, and return the first k most frequent elements.

What I learned:
- Use a dictionary to count the frequency of each element
- `count.items()` returns `(key, value)` pairs
- `sorted()` can sort dictionary items using a custom key
- `lambda item: item[1]` sorts by frequency instead of the number
- `reverse=True` sorts in descending order
- `list[:k]` returns the first k elements
- `lambda` is an anonymous function and can replace a simple helper function

Important Example:

```python
count = {}

for num in nums:
    count[num] = count.get(num, 0) + 1
```

Frequency Result:

```python
{
    1: 3,
    2: 2,
    3: 1
}
```

Sorting Example:

```python
sorted_items = sorted(
    count.items(),
    key=lambda item: item[1],
    reverse=True
)
```

Result:

```python
[(1, 3), (2, 2), (3, 1)]
```

Slicing Example:

```python
sorted_items[:2]
```

Result:

```python
[(1, 3), (2, 2)]
```

Time Complexity:
- O(n log n)

Space Complexity:
- O(n)