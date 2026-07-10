# LeetCode Learning Log

## 2026-06-27
### LeetCode 1 - Two Sum

Topic:
- Array
- Hash Table

Key Idea:
Use a dictionary called `seen` to store each previously visited number and its index. For each number, calculate the value needed to reach the target. If that value is already in `seen`, return the two indices.

What I learned:
- A dictionary can store both a number and its index
- `enumerate(nums)` provides the index and value during iteration
- Hash tables can reduce the time complexity from O(n²) to O(n)
- The needed value can be calculated with `target - num`
- Dictionary membership checks are usually O(1)

Important Example:

```python
nums = [2, 7, 11, 15]
target = 9

seen = {}

for index, num in enumerate(nums):
    need = target - num

    if need in seen:
        return [seen[need], index]

    seen[num] = index
```

Result:

```python
[0, 1]
```

Time Complexity:
- O(n)

Space Complexity:
- O(n)


## 2026-06-28
### LeetCode 217 - Contains Duplicate

Topic:
- Array
- Hash Table
- Set

Key Idea:
Use a set called `seen` to store numbers that have already appeared. If the current number is already in the set, a duplicate exists. Otherwise, add the number to the set.

What I learned:
- A dictionary stores key-value pairs
- A set stores unique values
- A set is useful when only checking whether a value already exists
- Sets use `add()` instead of `append()`
- `return False` must be outside the loop because every number must be checked

Important Example:

```python
nums = [1, 2, 3, 1]
seen = set()

for num in nums:
    if num in seen:
        return True

    seen.add(num)

return False
```

Result:

```python
True
```

Time Complexity:
- O(n)

Space Complexity:
- O(n)


## 2026-07-01
### LeetCode 242 - Valid Anagram

Topic:
- Hash Table
- Dictionary
- Frequency Count

Key Idea:
Use a dictionary to count the characters in the first string. Then subtract the character counts while reading the second string. The two strings are anagrams only when all character frequencies match.

What I learned:
- `dict.get(key, 0)` returns the current value when the key exists
- It returns the default value `0` when the key does not exist
- Frequency counting often uses `count[key] = count.get(key, 0) + 1`
- Character counts can be increased for one string and decreased for another
- Strings with different lengths cannot be anagrams

Important Example:

```python
s = "anagram"
t = "nagaram"

char_count = {}

for char in s:
    char_count[char] = char_count.get(char, 0) + 1

for char in t:
    char_count[char] = char_count.get(char, 0) - 1
```

Result:

```python
True
```

Time Complexity:
- O(n)

Space Complexity:
- O(1) when only lowercase English letters are used
- O(k) for a general character set


## 2026-07-01
### LeetCode 383 - Ransom Note

Topic:
- Hash Table
- Dictionary
- Frequency Count

Key Idea:
Count the available characters in `magazine`, then use each character in `ransomNote` to reduce the corresponding count. If a required character is unavailable, return `False`.

What I learned:
- A dictionary can track how many times each character is available
- `char_count[char] -= 1` means one available character has been used
- Characters cannot be reused after their count reaches zero
- A frequency dictionary is necessary when repeated values matter
- A set is not enough because it does not store frequency

Important Example:

```python
ransomNote = "aa"
magazine = "aab"

char_count = {}

for char in magazine:
    char_count[char] = char_count.get(char, 0) + 1

for char in ransomNote:
    if char not in char_count or char_count[char] == 0:
        return False

    char_count[char] -= 1
```

Result:

```python
True
```

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
Use a dictionary to group words by their sorted character sequence. Words that are anagrams produce the same sorted string and therefore share the same dictionary key.

What I learned:
- A dictionary can group multiple values under one key
- A set is better for checking existence, while a dictionary is better for grouping
- Lists use `append()`, while sets use `add()`
- `sorted(word)` returns a sorted list of characters
- `"".join(sorted(word))` converts the character list into a string
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
Count the frequency of each number using a dictionary, sort the dictionary items by frequency in descending order, and return the first `k` numbers.

What I learned:
- A dictionary can count the frequency of each element
- `count.items()` returns `(key, value)` pairs
- `sorted()` can use a custom sorting key
- `lambda item: item[1]` sorts by frequency instead of by number
- `reverse=True` sorts values in descending order
- `list[:k]` returns the first `k` elements
- A lambda expression is a small anonymous function

Important Example:

```python
count = {}

for num in nums:
    count[num] = count.get(num, 0) + 1

sorted_items = sorted(
    count.items(),
    key=lambda item: item[1],
    reverse=True
)
```

Result:

```python
nums = [1, 1, 1, 2, 2, 3]
k = 2

sorted_items
# [(1, 3), (2, 2), (3, 1)]

sorted_items[:k]
# [(1, 3), (2, 2)]
```

Time Complexity:
- O(n log n)

Space Complexity:
- O(n)


## 2026-07-09
### LeetCode 128 - Longest Consecutive Sequence

Topic:
- Array
- Hash Set
- Sequence Detection

Key Idea:
Convert the input list into a set for fast membership checks. A number is the beginning of a consecutive sequence only when `num - 1` is not in the set. From each sequence beginning, repeatedly check whether the next number exists and count the sequence length.

What I learned:
- Converting a list into a set allows average O(1) membership checks
- `current_num` is a variable that tracks the current number in a sequence
- `current_length` stores the length of the sequence currently being explored
- `longest` stores the longest sequence length found so far
- `if` checks once whether a number is a sequence starting point
- `while` repeatedly moves forward while consecutive numbers exist
- A problem may contain multiple sequence starting points
- The outer `for` loop checks every possible starting point
- `longest = max(longest, current_length)` keeps the larger of the previous best length and the current sequence length
- `current_num += 1` and `current_length += 1` update variables, while expressions such as `current_num + 1` alone do not change them

Important Example:

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                longest = max(longest, current_length)

        return longest
```

Result:

```python
nums = [100, 4, 200, 1, 3, 2]

# Consecutive sequences:
# [1, 2, 3, 4]
# [100]
# [200]

# Longest sequence length:
4
```

Time Complexity:
- O(n)

Space Complexity:
- O(n)