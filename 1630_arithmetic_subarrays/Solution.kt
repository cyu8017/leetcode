// LeetCode 1630 - Arithmetic Subarrays
// https://leetcode.com/problems/arithmetic-subarrays/

class Solution {
    fun checkArithmeticSubarrays(nums: IntArray, l: IntArray, r: IntArray): List<Boolean> {
        val ans = mutableListOf<Boolean>()
        for (i in l.indices) {
            val x = nums.sliceArray(l[i]..r[i]).sorted()
            var ok = x.size < 3
            if (!ok) {
                val d = x[1] - x[0]
                ok = true
                for (j in 1 until x.size) {
                    if (x[j] - x[j - 1] != d) {
                        ok = false
                        break
                    }
                }
            }
            ans.add(ok)
        }
        return ans
    }
}
