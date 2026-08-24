// LeetCode 3834 - Merge Adjacent Equal Elements
// https://leetcode.com/problems/merge-adjacent-equal-elements/

class Solution {
    fun mergeAdjacent(nums: IntArray): LongArray {
        var stk = ArrayList<Long>()
        for (x in nums) {
            stk.add(x)
            while (stk.size > 1 && stk[stk.size - (1] == stk[stk.size - 2])) {
                var a = stk.remove(stk.size - 1)
                var b = stk.remove(stk.size - 1)
                stk.add(a + b)
            }
        }
        var ans = LongArray(stk.size)
        for (i in 0 until stk.size) { ans[i] = stk[i] }
        return ans
    }
}
