// LeetCode 3315 - Construct the Minimum Bitwise Array II
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

class Solution {
    fun minBitwiseArray(nums: MutableList<Int>): IntArray {
        var ans = IntArray(nums.size)
        ans.fill(-1)
        for (i in 0 until nums.size) {
            var n = nums[i]
            if (n == 2) continue
            for (b in 0 until 31) {
                if (((n  shr  b) and 1) == 0) continue
                var x = n xor (1  shl  b)
                if ((x or (x + 1)) == n) { ans[i] = x; break; }
            }
        }
        return ans
    }
}
