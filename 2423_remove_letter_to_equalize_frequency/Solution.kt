// LeetCode 2423 - Remove Letter To Equalize Frequency
// https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution {
    fun equalFrequency(word: String): Boolean {
        for (skip in word.indices) {
            val cnt = IntArray(26)
            for (i in word.indices) {
                if (i == skip) continue
                cnt[word[i] - 'a']++
            }
            val freq = HashMap<Int, Int>()
            for (c in cnt) if (c > 0) freq[c] = freq.getOrDefault(c, 0) + 1
            if (freq.size == 1) return true
        }
        return false
    }
}
