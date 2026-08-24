// LeetCode 3533 - Concatenated Divisibility
// https://leetcode.com/problems/concatenated-divisibility/

class Solution {
    var n = 0
    var k = 0
    lateinit var nums: IntArray
    lateinit var pows: IntArray
    lateinit var memo: HashMap<Long, Boolean>

    fun concatenatedDivisibility(nums: IntArray, k: Int): IntArray {
        nums.sort()
        this.nums = nums
        this.k = k
        n = nums.size
        pows = IntArray(n)
        for (i in 0 until n) {
            var p = 1
            val num = nums[i]
            if (num == 0) p = 10 % k
            else {
                var x = num
                while (x > 0) {
                    p = p * 10 % k
                    x /= 10
                }
            }
            pows[i] = p
        }
        memo = HashMap()
        if (!dp(0, 0)) return IntArray(0)
        val res = reconstruct(0, 0)
        return res.toIntArray()
    }

    fun dp(mask: Int, mod: Int): Boolean {
        if (mask == (1 shl n) - 1) return mod == 0
        val key = (mask.toLong() shl 32) or mod.toLong()
        memo[key]?.let { return it }
        for (i in 0 until n) {
            if (((mask shr i) and 1) == 0) {
                val nm = (mod * pows[i] + nums[i]) % k
                if (dp(mask or (1 shl i), nm)) {
                    memo[key] = true
                    return true
                }
            }
        }
        memo[key] = false
        return false
    }

    fun reconstruct(mask: Int, mod: Int): ArrayList<Int> {
        for (i in 0 until n) {
            if (((mask shr i) and 1) == 0) {
                val nm = (mod * pows[i] + nums[i]) % k
                if (dp(mask or (1 shl i), nm)) {
                    val rest = reconstruct(mask or (1 shl i), nm)
                    rest.add(0, nums[i])
                    return rest
                }
            }
        }
        return ArrayList()
    }
}
