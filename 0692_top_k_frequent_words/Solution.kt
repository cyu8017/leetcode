// LeetCode 0692 - Top K Frequent Words
// https://leetcode.com/problems/top-k-frequent-words/

class Solution {
    fun topKFrequent(words: Array<String>, k: Int): List<String> {
        val counts = HashMap<String, Int>()
        for (word in words) counts[word] = counts.getOrDefault(word, 0) + 1
        val ordered = ArrayList(counts.keys)
        ordered.sortWith { a, b ->
            val ca = counts[a]!!
            val cb = counts[b]!!
            if (ca != cb) cb.compareTo(ca) else a.compareTo(b)
        }
        return ordered.subList(0, k)
    }
}
