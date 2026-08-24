// LeetCode 3896 - Minimum Operations To Transform Array Into Alternating Prime
// https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/

class Solution {
    private val MX: Int = 200000
    private var isPrime: BooleanArray? = null
    private var primes: MutableList<Int>? = null
    private var ready: Boolean = false

    private fun init() {
        if (ready) return
        isPrime = BooleanArray(MX + 1)
        for (i in 0..MX) { isPrime[i] = true }
        isPrime[0] = isPrime[1] = false
        for (i in 2..MX / i) {
            if (isPrime[i]) {
                run {
                    var j = i * i
                    while (j <= MX) {
                        isPrime[j] = false
                        j += i
                    }
                }
            }
        }
        primes = ArrayList()
        for (i in 2..MX) { if (isPrime[i]) primes.add(i) }
        ready = true
    }

    fun minOperations(nums: IntArray): Int {
        init()
        var ans = 0
        for (i in 0 until nums.size) {
            var x = nums[i]
            if (i % 2 == 0) {
                var idx = Collections.binarySearch(primes, x)
                if (idx < 0) idx = ~idx
                ans += primes[idx] - x
            } else if (isPrime[x]) {
                ans +=if ((x == 2)) 2 else 1
            }
        }
        return ans
    }
}
