// LeetCode 0932 - Beautiful Array
// https://leetcode.com/problems/beautiful-array/

class Solution {
    fun beautifulArray(n: Int): IntArray {
        if (n == 1) return intArrayOf(1)
        var left = beautifulArray((n + 1) / 2)
        var right = beautifulArray(n / 2)
        var ans = IntArray(n)
        var k = 0
        for (x in left) { ans[k++] = 2 * x - 1; }
        for (x in right) { ans[k++] = 2 * x; }
        return ans
    }
}
