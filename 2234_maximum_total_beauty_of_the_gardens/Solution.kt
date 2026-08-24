// LeetCode 2234 - Maximum Total Beauty of the Gardens
// https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/

class Solution {

    fun maximumBeauty(flowers: IntArray, newFlowers: Long, target: Int, full: Int, partial: Int): Long {

            var n = flowers.size
            for (i in 0 until n) { if (flowers[i] > target) flowers[i] = target }
            flowers.sort()
            var sum = 0
            for (f in flowers) sum += f
            if (target * n - sum <= newFlowers) return n * full
            var pref = LongArray(n + 1)
            for (i in 0 until n) { pref[i + 1] = pref[i] + flowers[i] }
            var ans = 0
            var j = n - 1
            var remain = newFlowers
            for (complete in 0..n) {
                if (complete > 0) {
                    var need = target - flowers[n - complete]
                    if (remain < need) break
                    remain -= need
                }
                while (j >= n - complete || (j >= 0 && flowers[j] * (j + 1) - pref[j + 1] > remain)) j--
                var partialVal = 0
                if (j >= 0) {
                    var extra = (remain - (flowers[j] * (j + 1) - pref[j + 1])) / (j + 1)
                    partialVal = flowers[j] + extra
                    if (partialVal >= target) partialVal = target - 1
                }
                ans = maxOf(ans, complete * full + partialVal * partial)
            }
            return ans

    }

}
