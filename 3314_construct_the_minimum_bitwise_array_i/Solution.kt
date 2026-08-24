// LeetCode 3314 - Construct the Minimum Bitwise Array I
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

class Solution {
    fun minBitwiseArray(nums: MutableList<Int>): IntArray {
        var ans = IntArray(nums.size)
        ans.fill(-1)
        for (i in 0 until nums.size) {
            var n = nums[i]
            for (x in 0 until n) {
                if ((x or (x + 1)) == n) { ans[i] = x; break; }
            }
        }
        return ans
    }
}
