// LeetCode 2137 - Pour Water Between Buckets to Make Water Levels Equal
// https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/

class Solution {
    fun equalizeWater(buckets: IntArray, loss: Int): Double {
        var lo: Double = 0, hi = 0
        for (b in buckets) hi = maxOf(hi, (double) b)
        for (iter in 0 until 60) {
            var mid: Double = (lo + hi) / 2
            var have: Double = 0, need = 0
            for (b in buckets) {
                if (b >= mid) have += b - mid
                else need += mid - b
            }
            if (have * (1.0 - loss / 100.0) >= need) lo = mid
            else hi = mid
        }
        return lo
    }
}
