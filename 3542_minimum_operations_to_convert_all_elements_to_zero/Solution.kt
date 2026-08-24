// LeetCode 3542 - Minimum Operations to Convert All Elements to Zero
// https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

class Solution {
    fun minOperations(nums: IntArray): Int {
        var stk = ArrayList<Int>()
        var ans = 0
        for (x in nums) {
            while (stk.size > 0 && stk[stk.size - 1] > x) {
                ans = ans + 1
                stk.remove(stk.size - 1)
            }
            if (x != 0 && (stk.size == 0 || stk[stk.size - 1] != x)) stk.add(x)
        }
        ans += stk.size
        return ans
    }
}
