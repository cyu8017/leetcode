// LeetCode 3557 - Find Maximum Number of Non Intersecting Substrings
// https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/

class Solution {
    fun maxSubstrings(word: String): Int {
        var ans = 0
        var first = HashMap<Int, Int>()
        for (i in 0 until word.length) {
            var c = word[i]
            if (!first.containsKey(c)) first[c] = i
            else if (i - first[c] + 1 >= 4) {
                ans = ans + 1
                first.clear()
            }
        }
        return ans
    }
}
