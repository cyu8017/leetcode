// LeetCode 2763 - Sum of Imbalance Numbers of All Subarrays
// https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/

class Solution {
    fun sumImbalanceNumbers(nums: IntArray): Int {
        var n = nums.size
        var ans = 0
        for (i in 0 until n) {
            var seen = HashSet<Int>()
            var sortedVals = TreeSet<Int>()
            var imbalance = 0
            for (j in i until n) {
                var x = nums[j]
                if (!seen.contains(x)) {
                    seen.add(x)
                    var next = sortedVals.ceiling(x)
                    var prev = sortedVals.floor(x)
                    if (prev != null && x - prev != 1) imbalance++
                    if (next != null && next - x != 1) imbalance++
                    if (prev != null && next != null && next - prev > 1) imbalance--
                    sortedVals.add(x)
                }
                ans += imbalance
            }
        }
        return ans
    }
}
