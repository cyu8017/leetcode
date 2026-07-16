# 0737. Sentence Similarity II

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/sentence-similarity-ii/](https://leetcode.com/problems/sentence-similarity-ii/)
- **Premium:** Yes
- **Tags:** array, hash-table, string, depth-first-search, breadth-first-search, union-find

## Problem

We can represent a sentence as an array of words, for example, the sentence `"I am happy with leetcode"` can be represented as `arr = ["I","am",happy","with","leetcode"]`.

Given two sentences `sentence1` and `sentence2` each represented as a string array and given an array of string pairs `similarPairs` where `similarPairs[i] = [x_{i}, y_{i}]` indicates that the two words `x_{i}` and `y_{i}` are similar.

Return `true`* if `sentence1` and `sentence2` are similar, or *`false`* if they are not similar*.

Two sentences are similar if:

	- They have **the same length** (i.e., the same number of words)

	- `sentence1[i]` and `sentence2[i]` are similar.

Notice that a word is always similar to itself, also notice that the similarity relation is transitive. For example, if the words `a` and `b` are similar, and the words `b` and `c` are similar, then `a` and `c` are **similar**.



**Example 1:**

**Input:** sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]
**Output:** true
**Explanation:** The two sentences have the same length and each word i of sentence1 is also similar to the corresponding word in sentence2.

**Example 2:**

**Input:** sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","onepiece"],["platform","anime"],["leetcode","platform"],["anime","manga"]]
**Output:** true
**Explanation:** "leetcode" --> "platform" --> "anime" --> "manga" --> "onepiece".
Since "leetcode is similar to "onepiece" and the first two words are the same, the two sentences are similar.

**Example 3:**

**Input:** sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","hunterXhunter"],["platform","anime"],["leetcode","platform"],["anime","manga"]]
**Output:** false
**Explanation:** "leetcode" is not similar to "onepiece".



**Constraints:**

	- `1 <= sentence1.length, sentence2.length <= 1000`

	- `1 <= sentence1[i].length, sentence2[i].length <= 20`

	- `sentence1[i]` and `sentence2[i]` consist of lower-case and upper-case English letters.

	- `0 <= similarPairs.length <= 2000`

	- `similarPairs[i].length == 2`

	- `1 <= x_{i}.length, y_{i}.length <= 20`

	- `x_{i}` and `y_{i}` consist of English letters.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Consider the graphs where each pair in "pairs" is an edge.  Two words are similar if they are the same, or are in the same connected component of this graph.

## Approach

<!-- Describe your solution approach here -->
