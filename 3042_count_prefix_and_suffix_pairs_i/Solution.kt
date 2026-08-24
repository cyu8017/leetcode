// LeetCode 3042 - Count Prefix and Suffix Pairs I
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

class Solution {
    fun countPrefixSuffixPairs(words: Array<String>): Int {
        var ans = 0
        for (i in 0 until words.size) {
            var s = words[i]
            for (j in i + 1 until words.size) {
                var t = words[j]
                if (t.length() >= s.length() && t.startsWith(s) && t.endsWith(s))
                    ans++
            }
        }
        return ans
    }
}
