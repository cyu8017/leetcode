// LeetCode 3113 - Find the Number of Subarrays Where Boundary Elements Are Maximum
// https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/

class Solution {
    fun numberOfSubarrays(nums: IntArray): Long {
        var stk = ArrayDeque<IntArray>()
        var ans = 0
        for (x in nums) {
            while (!stk.isEmpty() && stk.peekLast()[0] < x) stk.pollLast()
            if (stk.isEmpty() || stk.peekLast()[0] > x) stk.addLast(intArrayOf(x, 1))
            else stk.peekLast()[1]++
            ans += stk.peekLast()[1]
        }
        return ans
    }
}
