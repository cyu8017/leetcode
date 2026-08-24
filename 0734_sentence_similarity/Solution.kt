// LeetCode 0734 - Sentence Similarity
// https://leetcode.com/problems/sentence-similarity/

class Solution {
    fun areSentencesSimilar(sentence1: Array<String>, sentence2: Array<String>, similarPairs: MutableList<MutableList<String>>): Boolean {
        if (sentence1.size != sentence2.size) return false
        var pairs = HashSet<String>()
        for (pair in similarPairs) {
            pairs.add(pair[0] + "#" + pair[1])
            pairs.add(pair[1] + "#" + pair[0])
        }
        for (i in 0 until sentence1.size) {
            if (!sentence1[(i] == sentence2[i]) && !pairs.contains(sentence1[i] + "#" + sentence2[i])) return false
        }
        return true
    }
}
