// LeetCode 0548 - Split Array with Equal Sum
// https://leetcode.com/problems/split-array-with-equal-sum/

class Solution {
    fun splitArray(nums: IntArray): Boolean {
        val n = nums.size
        if (n < 7) {
            return false
        }

        val prefix = IntArray(n + 1)
        for (i in nums.indices) {
            prefix[i + 1] = prefix[i] + nums[i]
        }

        for (j in 3 until n - 3) {
            val seen = HashSet<Int>()
            for (i in 1 until j - 1) {
                val first = prefix[i] - prefix[0]
                val second = prefix[j] - prefix[i + 1]
                if (first == second) {
                    seen.add(first)
                }
            }

            for (k in j + 2 until n - 1) {
                val third = prefix[k] - prefix[j + 1]
                val fourth = prefix[n] - prefix[k + 1]
                if (third == fourth && third in seen) {
                    return true
                }
            }
        }

        return false
    }
}
