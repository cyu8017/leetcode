// LeetCode 3685 - Subsequence Sum After Capping Elements
// https://leetcode.com/problems/subsequence-sum-after-capping-elements/

class Solution {
    fun subsequenceSumAfterCapping(nums: IntArray, k: Int): BooleanArray {
        val n = nums.size
        val sorted = nums.clone()
        sorted.sort()
        val ans = BooleanArray(n)
        val reach = BooleanArray(k + 1)
        reach[0] = true
        var idx = 0
        for (x in 1..n) {
            while (idx < n && sorted[idx] <= x) {
                val v = sorted[idx]
                for (s in k downTo v) {
                    if (reach[s - v]) reach[s] = true
                }
                idx++
            }
            val tmp = reach.clone()
            val rem = n - idx
            for (s in 0..k) {
                if (!reach[s]) continue
                var t = 1
                while (t <= rem && s + t * x <= k) {
                    tmp[s + t * x] = true
                    t++
                }
            }
            ans[x - 1] = tmp[k]
        }
        return ans
    }
}
