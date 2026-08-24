// LeetCode 3591 - Check if Any Element Has Prime Frequency
// https://leetcode.com/problems/check-if-any-element-has-prime-frequency/

class Solution {
    fun isPrime(x: Int): Boolean {
        if (x < 2) return false
        var i: Int = 2
while (i * i <= x) {

            if (x % i == 0) return false
        return true
    }
    fun checkPrimeFrequency(nums: IntArray): Boolean {
        var cnt = HashMap<Int, Int>()
        for (x in nums) {
            if (!cnt.containsKey(x)) cnt[x] = 0
            cnt[x] = cnt[x] + 1
        }
        for (kv in cnt)
            if (isPrime(kv.value)) return true
        return false
    }
}
i = i + 1
}
