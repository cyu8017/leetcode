# 1258. Synonymous Sentences

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/synonymous-sentences/](https://leetcode.com/problems/synonymous-sentences/)
- **Premium:** Yes
- **Tags:** array, hash-table, string, backtracking, sort, union-find

## Problem

You are given a list of equivalent string pairs `synonyms` where `synonyms[i] = [s_{i}, t_{i}]` indicates that `s_{i}` and `t_{i}` are equivalent strings. You are also given a sentence `text`.

Return *all possible synonymous sentences **sorted lexicographically***.



**Example 1:**

**Input:** synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]], text = "I am happy today but was sad yesterday"
**Output:** ["I am cheerful today but was sad yesterday","I am cheerful today but was sorrow yesterday","I am happy today but was sad yesterday","I am happy today but was sorrow yesterday","I am joy today but was sad yesterday","I am joy today but was sorrow yesterday"]

**Example 2:**

**Input:** synonyms = [["happy","joy"],["cheerful","glad"]], text = "I am happy today but was sad yesterday"
**Output:** ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]



**Constraints:**

	- `0 <= synonyms.length <= 10`

	- `synonyms[i].length == 2`

	- `1 <= s_{i}.length,_{ }t_{i}.length <= 10`

	- `s_{i} != t_{i}`

	- `text` consists of at most `10` words.

	- All the pairs of `synonyms` are **unique**.

	- The words of `text` are separated by single spaces.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Find all synonymous groups of words.
2. Use union-find data structure.
3. By backtracking, generate all possible statements.

## Approach

<!-- Describe your solution approach here -->
