// LeetCode 1477 - Find Two Non-overlapping Sub-arrays Each With Target Sum
// https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

class Solution {
    fun minSumOfLengths(arr: IntArray, target: Int): Int {
        val inf = 1_000_000_000
        var left = 0
        var total = 0
        var best = inf
        var ans = inf
        val shortest = IntArray(arr.size) { inf }
        for (right in arr.indices) {
            total += arr[right]
            while (total > target) {
                total -= arr[left]
                left++
            }
            if (total == target) {
                val length = right - left + 1
                if (left > 0) ans = minOf(ans, length + shortest[left - 1])
                best = minOf(best, length)
            }
            shortest[right] = best
        }
        return if (ans == inf) -1 else ans
    }
}
