# 1177. Can Make Palindrome from Substring

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/can-make-palindrome-from-substring/](https://leetcode.com/problems/can-make-palindrome-from-substring/)
- **Tags:** array, hash-table, string, bit-manipulation, prefix-sum

## Problem

You are given a string `s` and array `queries` where `queries[i] = [left_{i}, right_{i}, k_{i}]`. We may rearrange the substring `s[left_{i}...right_{i}]` for each query and then choose up to `k_{i}` of them to replace with any lowercase English letter.

If the substring is possible to be a palindrome string after the operations above, the result of the query is `true`. Otherwise, the result is `false`.

Return a boolean array `answer` where `answer[i]` is the result of the `i^{th}` query `queries[i]`.

Note that each letter is counted individually for replacement, so if, for example `s[left_{i}...right_{i}] = "aaa"`, and `k_{i} = 2`, we can only replace two of the letters. Also, note that no query modifies the initial string `s`.

**Example :**

```
**Input:** s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
**Output:** [true,false,false,true,true]
**Explanation:**
queries[0]: substring = "d", is palidrome.
queries[1]: substring = "bc", is not palidrome.
queries[2]: substring = "abcd", is not palidrome after replacing only 1 character.
queries[3]: substring = "abcd", could be changed to "abba" which is palidrome. Also this can be changed to "baab" first rearrange it "bacd" then replace "cd" with "ab".
queries[4]: substring = "abcda", could be changed to "abcba" which is palidrome.
```

**Example 2:**

```
**Input:** s = "lyb", queries = [[0,1,0],[2,2,1]]
**Output:** [false,true]
```

**Constraints:**

- `1 <= s.length, queries.length <= 10^{5}`

	- `0 <= left_{i} <= right_{i} < s.length`

	- `0 <= k_{i} <= s.length`

	- `s` consists of lowercase English letters.

### Hints

1. Since we can rearrange the substring, all we care about is the frequency of each character in that substring.
2. How to find the character frequencies efficiently ?
3. As a preprocess, calculate the accumulate frequency of all characters for all prefixes of the string.
4. How to check if a substring can be changed to a palindrome given its characters frequency ?
5. Count the number of odd frequencies, there can be at most one odd frequency in a palindrome.

## Approach

<!-- Describe your solution approach here -->
