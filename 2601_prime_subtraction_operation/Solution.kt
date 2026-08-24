// LeetCode 2601 - Prime Subtraction Operation
// https://leetcode.com/problems/prime-subtraction-operation/

class Solution {
    fun primeSubOperation(nums: IntArray): Boolean {
        val maxV = nums.maxOrNull() ?: 0
        val isP = BooleanArray(maxV + 1) { true }
        if (maxV >= 0) isP[0] = false
        if (maxV >= 1) isP[1] = false
        var i = 2
        while (i * i <= maxV) {
            if (isP[i]) {
                var j = i * i
                while (j <= maxV) {
                    isP[j] = false
                    j += i
                }
            }
            i += 1
        }
        val primes = ArrayList<Int>()
        for (p in 2..maxV) if (isP[p]) primes.add(p)
        var prev = 0
        for (x in nums) {
            var best = -1
            for (p in primes) {
                if (p >= x) break
                if (x - p > prev) best = x - p
            }
            val cur = if (best != -1) best else x
            if (cur <= prev) return false
            prev = cur
        }
        return true
    }
}
