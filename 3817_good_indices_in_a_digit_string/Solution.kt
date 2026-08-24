// LeetCode 3817 - Good Indices In A Digit String
// https://leetcode.com/problems/good-indices-in-a-digit-string/

class Solution {
    fun goodIndices(s: String): IntArray {
        var ans = ArrayList<Int>()
        for (i in 0 until s.length) {
            var t = i.toString()
            var k = t.length
            if (i + 1 - k >= 0 && s.substring(i + 1 - k, k) == t) ans.add(i)
        }
        return ans.toIntArray()
    }
}
