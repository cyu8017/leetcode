// LeetCode 3806 - Maximum Bitwise And After Increment Operations
// https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/

class Solution {
    private fun bitLen(x0: Int): Int {
        var x = x0
        if (x == 0) return 0
        var n = 0
        while (x > 0) {
            n++
            x = x shr 1
        }
        return n
    }

    fun maximumAND(nums: IntArray, k: Int, m: Int): Int {
        var mxVal = nums[0]
        for (v in nums) if (v > mxVal) mxVal = v
        mxVal += k
        val mx = bitLen(mxVal)
        var ans = 0
        val cost = IntArray(nums.size)
        for (bit in mx - 1 downTo 0) {
            val target = ans or (1 shl bit)
            for (i in nums.indices) {
                val x = nums[i]
                val j = bitLen(target and x.inv())
                val mask = (1 shl j) - 1
                cost[i] = (target and mask) - (x and mask)
            }
            cost.sort()
            var sum = 0
            for (i in 0 until m) sum += cost[i]
            if (sum <= k) ans = target
        }
        return ans
    }
}
