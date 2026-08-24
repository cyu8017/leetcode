// LeetCode 3480 - Maximize Subarrays After Removing One Conflicting Pair
// https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/

class Solution {
    fun maxSubarrays(n: Int, conflictingPairs: Array<IntArray>): Long {
        val m = conflictingPairs.size
        var best = 0L
        for (skip in 0 until m) {
            val rightLimit = IntArray(n + 2) { n + 1 }
            for (i in 0 until m) {
                if (i == skip) continue
                var a = conflictingPairs[i][0]
                var b = conflictingPairs[i][1]
                if (a > b) {
                    val t = a
                    a = b
                    b = t
                }
                if (b < rightLimit[a]) rightLimit[a] = b
            }
            var minRight = n + 1
            var cnt = 0L
            for (l in n downTo 1) {
                if (rightLimit[l] < minRight) minRight = rightLimit[l]
                cnt += (minRight - l).toLong()
            }
            if (cnt > best) best = cnt
        }
        return best
    }
}
