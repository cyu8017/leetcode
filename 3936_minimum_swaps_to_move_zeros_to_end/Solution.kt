// LeetCode 3936 - Minimum Swaps To Move Zeros To End
// https://leetcode.com/problems/minimum-swaps-to-move-zeros-to-end/

class Solution {
    fun minimumSwaps(nums: IntArray): Int {
        var ans = 0
        val n = nums.size
        var i = 0
        var j = n - 1
        while (i < j) {
            while (i < n && nums[i] != 0) i++
            while (j > 0 && nums[j] == 0) j--
            if (i >= j) break
            ans++
            i++
            j--
        }
        return ans
    }
}
