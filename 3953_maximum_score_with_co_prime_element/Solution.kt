// LeetCode 3953 - Maximum Score with Co-Prime Element
// https://leetcode.com/problems/maximum-score-with-co-prime-element/

class Solution {
    fun maxScore(nums: IntArray, maxVal: Int): Int {
        var limit = maxVal
        val frequency = IntArray(100001)
        for (x in nums) {
            frequency[x]++
            if (x > limit) limit = x
        }
        val divisible = IntArray(limit + 1)
        for (d in 1..limit) {
            var multiple = d
            while (multiple <= limit) {
                if (multiple < frequency.size) divisible[d] += frequency[multiple]
                multiple += d
            }
        }
        var best = -nums.size
        val checked = BooleanArray(limit + 1)
        for (x in 1..maxVal) {
            best = maxOf(best, evaluate(x, x < frequency.size && frequency[x] > 0, checked, divisible))
        }
        for (x in nums) {
            best = maxOf(best, evaluate(x, true, checked, divisible))
        }
        return best
    }

    private fun evaluate(x: Int, exists: Boolean, checked: BooleanArray, divisible: IntArray): Int {
        if (checked[x]) return Int.MIN_VALUE / 4
        checked[x] = true
        val bad = badCount(x, divisible)
        val cost = if (exists) {
            if (x > 1) bad - 1 else 0
        } else {
            if (bad > 0) bad else 1
        }
        return x - cost
    }

    private fun badCount(x: Int, divisible: IntArray): Int {
        val primes = ArrayList<Int>()
        var y = x
        var p = 2
        while (1L * p * p <= y) {
            if (y % p == 0) {
                primes.add(p)
                while (y % p == 0) y /= p
            }
            p++
        }
        if (y > 1) primes.add(y)
        var bad = 0
        val psz = primes.size
        for (mask in 1 until (1 shl psz)) {
            var product = 1
            var bits = 0
            for (i in 0 until psz) {
                if (((mask shr i) and 1) != 0) {
                    product *= primes[i]
                    bits++
                }
            }
            if (bits % 2 == 1) bad += divisible[product] else bad -= divisible[product]
        }
        return bad
    }
}
