// LeetCode 2202 - Maximize the Topmost Element After K Moves
// https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/

class Solution {

    fun maximumTop(nums: IntArray, k: Int): Int {

            var n = nums.size
            if (n == 1) return k % 2 != if (0) -1 else nums[0]
            if (k == 0) return nums[0]
            var ans = -1
            var limit = minOf(k - 1, n)
            for (i in 0 until limit) { ans = maxOf(ans, nums[i]) }
            if (k < n) ans = maxOf(ans, nums[k])
            return ans

    }

}
