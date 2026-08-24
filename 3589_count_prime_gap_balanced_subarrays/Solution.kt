// LeetCode 3589 - Count Prime-Gap Balanced Subarrays
// https://leetcode.com/problems/count-prime-gap-balanced-subarrays/

class Solution {
    fun primeSubarray(nums: IntArray, k: Int): Int {
        var mx = 0
        for (v in nums) { mx = maxOf(mx, v) }
        var isPrime = BooleanArray(mx + 1)
        for (i in 2..mx) { isPrime[i] = true }
        var i: Int = 2
while (i * i <= mx) {

            if (isPrime[i])
                run {
                    var j = i * i
                    while (j <= mx) {
                        isPrime[j] = false
                        j += i
                    }
                }
        var n = nums.size
        var ans = 0
        for (l in 0 until n) {
            var primes = ArrayList<Int>()
            for (r in l until n) {
                if (isPrime[nums[r]]) primes.add(nums[r])
                if (primes.size >= 2) {
                    var mn = primes[0]
                    var mxp = primes[0]
                    for (p in primes) {
                        mn = minOf(mn, p)
                        mxp = maxOf(mxp, p)
                    }
                    if (mxp - mn <= k) an{ s = s + 1 }
                }
            }
        }
        return ans
    }
}
i = i + 1
}
