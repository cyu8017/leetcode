// LeetCode 0830 - Positions of Large Groups
// https://leetcode.com/problems/positions-of-large-groups/

class Solution {
    fun largeGroupPositions(s: String): MutableList<MutableList<Int>> {
        var ans = ArrayList<MutableList<Int>>()
        var n = s.length, i = 0
        while (i < n) {
            var j = i
            while (j < n && s[j] == s[i]) j++
            if (j - i >= 3) ans.add(i, j - 1))
            i = j
        }
        return ans
    }
}
