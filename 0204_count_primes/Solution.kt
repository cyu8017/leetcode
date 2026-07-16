// LeetCode 0204 - Count Primes\n// https://leetcode.com/problems/\n\nclass Solution {
    fun countPrimes(n: Int): Int {
        if (n <= 2) return 0
        val prime = BooleanArray(n) { true }
        var p = 2
        while (p * p < n) { if (prime[p]) { var multiple = p * p; while (multiple < n) { prime[multiple] = false; multiple += p } }; p++ }
        return (2 until n).count { prime[it] }
    }
}
