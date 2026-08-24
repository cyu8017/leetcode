// LeetCode 0884 - Uncommon Words from Two Sentences
// https://leetcode.com/problems/uncommon-words-from-two-sentences/

class Solution {
    fun uncommonFromSentences(s1: String, s2: String): Array<String> {
        val count = HashMap<String, Int>()
        add(count, s1)
        add(count, s2)
        val ans = mutableListOf<String>()
        for ((k, v) in count) if (v == 1) ans.add(k)
        return ans.toTypedArray()
    }

    private fun add(count: HashMap<String, Int>, s: String) {
        for (w in s.split(" ")) {
            if (w.isEmpty()) continue
            count[w] = count.getOrDefault(w, 0) + 1
        }
    }
}
