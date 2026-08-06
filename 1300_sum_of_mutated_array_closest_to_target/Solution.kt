// LeetCode 1300 - Sum of Mutated Array Closest to Target
// https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

class Solution {
    fun findBestValue(arr: IntArray, target: Int): Int {
        var lo = 0
        var hi = arr.maxOrNull() ?: 0
        while (lo < hi) {
            val mid = (lo + hi) / 2
            var sum = 0L
            for (x in arr) sum += minOf(x, mid).toLong()
            if (sum < target) lo = mid + 1 else hi = mid
        }
        var before = 0L
        var after = 0L
        for (x in arr) {
            before += minOf(x, lo - 1).toLong()
            after += minOf(x, lo).toLong()
        }
        return if (target - before <= after - target) lo - 1 else lo
    }
}
