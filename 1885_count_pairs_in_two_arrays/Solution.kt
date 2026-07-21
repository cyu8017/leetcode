// LeetCode 1885 - Count Pairs in Two Arrays
// https://leetcode.com/problems/count-pairs-in-two-arrays/

class Solution {
    fun countPairs(nums1: IntArray, nums2: IntArray): Long {
        val diff = IntArray(nums1.size) { nums1[it] - nums2[it] }
        diff.sort()
        var answer = 0L
        val n = diff.size
        for (i in 0 until n) {
            val target = -diff[i]
            var lo = i + 1
            var hi = n
            while (lo < hi) {
                val mid = (lo + hi) ushr 1
                if (diff[mid] <= target) lo = mid + 1 else hi = mid
            }
            answer += (n - lo).toLong()
        }
        return answer
    }
}
