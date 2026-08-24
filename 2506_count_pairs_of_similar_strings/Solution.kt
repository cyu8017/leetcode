// LeetCode 2506 - Count Pairs Of Similar Strings
// https://leetcode.com/problems/count-pairs-of-similar-strings/

import java.util.HashMap

class Solution {
    fun similarPairs(words: Array<String>): Int {
            var freq: MutableMap<Int, Int> = HashMap()
            var ans: Int = 0
            for (w in words) {
                var mask: Int = 0
                for (c in w.toCharArray()) mask |= 1 << (c - 'a')
                ans +=freq.getOrDefault(mask, 0)
                freq.put(mask, freq.getOrDefault(mask, 0) + 1)
            }
            return ans
    }
}
