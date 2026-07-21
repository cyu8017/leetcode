// LeetCode 1889 - Minimum Space Wasted From Packaging
// https://leetcode.com/problems/minimum-space-wasted-from-packaging/

class Solution {
    fun minWastedSpace(packages: IntArray, boxes: Array<IntArray>): Int {
        packages.sort()
        val prefix = LongArray(packages.size)
        prefix[0] = packages[0].toLong()
        for (i in 1 until packages.size) {
            prefix[i] = prefix[i - 1] + packages[i]
        }
        var answer = Long.MAX_VALUE
        for (supplier in boxes) {
            supplier.sort()
            var start = 0
            var wasted = 0L
            for (box in supplier) {
                var lo = start
                var hi = packages.size
                while (lo < hi) {
                    val mid = (lo + hi) ushr 1
                    if (packages[mid] <= box) lo = mid + 1 else hi = mid
                }
                val end = lo
                if (end == start) continue
                val packageSum = prefix[end - 1] - if (start > 0) prefix[start - 1] else 0L
                wasted += box.toLong() * (end - start) - packageSum
                start = end
            }
            if (start == packages.size) {
                answer = minOf(answer, wasted)
            }
        }
        return if (answer == Long.MAX_VALUE) -1 else (answer % 1_000_000_007).toInt()
    }
}
