// LeetCode 1058 - Minimize Rounding Error to Meet Target
// https://leetcode.com/problems/minimize-rounding-error-to-meet-target/

class Solution {
    fun minimizeError(prices: Array<String>, target: Int): String {
        var floors = 0
        val fracs = mutableListOf<Double>()
        for (p in prices) {
            val value = p.toDouble()
            val floor = value.toInt()
            floors += floor
            val frac = value - floor
            if (frac > 1e-9) fracs.add(frac)
        }
        val ceilCount = target - floors
        if (ceilCount < 0 || ceilCount > fracs.size) return "-1"
        fracs.sortDescending()
        var error = 0.0
        for (i in fracs.indices) {
            val f = fracs[i]
            error += if (i < ceilCount) 1 - f else f
        }
        return String.format("%.3f", error)
    }
}
