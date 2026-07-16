# 0734. Sentence Similarity

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/sentence-similarity/](https://leetcode.com/problems/sentence-similarity/)
- **Premium:** Yes
- **Tags:** array, hash-table, string

## Problem

We can represent a sentence as an array of words, for example, the sentence `"I am happy with leetcode"` can be represented as `arr = ["I","am",happy","with","leetcode"]`.

Given two sentences `sentence1` and `sentence2` each represented as a string array and given an array of string pairs `similarPairs` where `similarPairs[i] = [x_{i}, y_{i}]` indicates that the two words `x_{i}` and `y_{i}` are similar.

Return *`true` if `sentence1` and `sentence2` are similar, or `false` if they are not similar*.

Two sentences are similar if:

	- They have **the same length** (i.e., the same number of words)

	- `sentence1[i]` and `sentence2[i]` are similar.

Notice that a word is always similar to itself, also notice that the similarity relation is not transitive. For example, if the words `a` and `b` are similar, and the words `b` and `c` are similar, `a` and `c` are **not necessarily similar**.



**Example 1:**

**Input:** sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]
**Output:** true
**Explanation:** The two sentences have the same length and each word i of sentence1 is also similar to the corresponding word in sentence2.

**Example 2:**

**Input:** sentence1 = ["great"], sentence2 = ["great"], similarPairs = []
**Output:** true
**Explanation:** A word is similar to itself.

**Example 3:**

**Input:** sentence1 = ["great"], sentence2 = ["doubleplus","good"], similarPairs = [["great","doubleplus"]]
**Output:** false
**Explanation:** As they don't have the same length, we return false.



**Constraints:**

	- `1 <= sentence1.length, sentence2.length <= 1000`

	- `1 <= sentence1[i].length, sentence2[i].length <= 20`

	- `sentence1[i]` and `sentence2[i]` consist of English letters.

	- `0 <= similarPairs.length <= 1000`

	- `similarPairs[i].length == 2`

	- `1 <= x_{i}.length, y_{i}.length <= 20`

	- `x_{i}` and `y_{i}` consist of lower-case and upper-case English letters.

	- All the pairs `(x_{i},_{ }y_{i})` are **distinct**.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Two words w1 and w2 are similar if and only if w1 == w2, (w1, w2) was a pair, or (w2, w1) was a pair.

## Approach

<!-- Describe your solution approach here -->
