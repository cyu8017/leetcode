// LeetCode 1713 - Minimum Operations to Make a Subsequence
// https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/

class Solution {
    fun minOperations(target: IntArray, arr: IntArray): Int {
        val pos = HashMap<Int, Int>()
        for (i in target.indices) {
            pos[target[i]] = i
        }
        val lis = IntArray(arr.size)
        var size = 0
        for (value in arr) {
            val idx = pos[value] ?: continue
            var lo = 0
            var hi = size
            while (lo < hi) {
                val mid = (lo + hi) ushr 1
                if (lis[mid] < idx) {
                    lo = mid + 1
                } else {
                    hi = mid
                }
            }
            lis[lo] = idx
            if (lo == size) {
                size++
            }
        }
        return target.size - size
    }
}
