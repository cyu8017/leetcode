// LeetCode 3971 - Maximum Total Value
// https://leetcode.com/problems/maximum-total-value/

class Solution {
    fun maximumTotalValue(value: IntArray, decay: IntArray, m: Long): Int {
        val mod = 1000000007
        if (countAtLeast(value, decay, 1) <= m) {
            var sum = 0
            for (i in 0 until value.size) {
                var terms = (value[i] - 1L) / decay[i] + 1
                sum = (sum + terms * value[i] - decay[i] * terms * (terms - 1) / 2) % mod
            }
            return sum
        }
        var high = 0
        for (v in value) { if (v > high) high = v }
        var low = 1
        while (low < high) {
            var mid = (low + high + 1) / 2
            if (countAtLeast(value, decay, mid) >= m) low = mid
            else high = mid - 1
        }
        var threshold = low
        var count = 0
        var sum = 0
        for (i in 0 until value.size) {
            if (value[i] < threshold) continue
            var terms = (value[i] - threshold) / decay[i] + 1
            count += terms
            sum = (sum + (terms * value[i] - decay[i] * terms * (terms - 1) / 2) % mod) % mod
        }
        sum = (sum - ((count - m) % mod) * (threshold % mod)) % mod
        if (sum < 0) sum += mod
        return sum
    }

    private fun countAtLeast(value: IntArray, decay: IntArray, threshold: Long): Long {
        var count = 0
        for (i in 0 until value.size) {
            if (value[i] >= threshold) count += (value[i] - threshold) / decay[i] + 1
        }
        return count
    }
}
