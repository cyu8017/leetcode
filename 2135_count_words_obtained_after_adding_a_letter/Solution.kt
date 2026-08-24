// LeetCode 2135 - Count Words Obtained After Adding a Letter
// https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

class Solution {
    fun mask(w: String): Int {
        var m: Int = 0
        for (i in 0 until w.length) m |= 1 << (w[i] - 'a')
        return m
    }

    fun wordCount(startWords: Array<String>, targetWords: Array<String>): Int {
        var have = HashSet()
        for (w in startWords) have.add(mask(w))
        var ans: Int = 0
        for (w in targetWords) {
            var m: Int = mask(w)
            for (i in 0 until w.length) {
                if (have.contains(m ^ (1 << (w[i] - 'a')))) { ans++; break; }
            }
        }
        return ans
    }
}
