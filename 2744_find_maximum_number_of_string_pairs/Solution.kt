// LeetCode 2744 - Find Maximum Number of String Pairs
// https://leetcode.com/problems/find-maximum-number-of-string-pairs/

class Solution {
    fun maximumNumberOfStringPairs(words: Array<String>): Int {
        var freq = HashMap<String, Int>()
        var ans = 0
        for (w in words) {
            var ca = w.toCharArray()
            var i = 0
            var j = ca.size - 1
            while (i < j) {
                var t = ca[i]
                ca[i] = ca[j]
                ca[j] = t
                i++, j--
            }
            var rev = String(ca)
            var c = freq.getOrDefault(rev, 0)
            if (c > 0) {
                ans++
                freq[rev] = c - 1
            } else {
                freq[w] = freq.getOrDefault(w, 0 + 1)
            }
        }
        return ans
    }
}
