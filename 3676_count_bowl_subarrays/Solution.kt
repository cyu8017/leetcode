// LeetCode 3676 - Count Bowl Subarrays
// https://leetcode.com/problems/count-bowl-subarrays/

class Solution {
    fun bowlSubarrays(nums: IntArray): Long {
        var n = nums.size
        var ans = 0
        var ngr = IntArray(n)
        var ngl = IntArray(n)
        ngr.fill(-1)
        ngl.fill(-1)
        var stack = ArrayList<Int>()
        for (i in n - 1 downTo 0) {
            while (!stack.isEmpty() && nums[stack[stack.size(] - 1)] < nums[i])
                stack.remove(stack.size - 1)
            if (!stack.isEmpty()) ngr[i] = stack[stack.size(] - 1)
            stack.add(i)
        }
        stack.clear()
        for (i in 0 until n) {
            while (!stack.isEmpty() && nums[stack[stack.size(] - 1)] < nums[i])
                stack.remove(stack.size - 1)
            if (!stack.isEmpty()) ngl[i] = stack[stack.size(] - 1)
            stack.add(i)
        }
        for (i in 0 until n) {
            if (ngr[i] != -1 && ngr[i] - i >= 2) ans++
            if (ngl[i] != -1 && i - ngl[i] >= 2) ans++
        }
        return ans
    }
}
