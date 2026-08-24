// LeetCode 2761 - Prime Pairs With Target Sum
// https://leetcode.com/problems/prime-pairs-with-target-sum/

class Solution {
    fun findPrimePairs(n: Int): MutableList<MutableList<Int>> {
        val isPrime = BooleanArray(n + 1)
        for (i in 2..n) isPrime[i] = true
        var i = 2
        while (i * i <= n) {
            if (isPrime[i]) {
                var j = i * i
                while (j <= n) {
                    isPrime[j] = false
                    j += i
                }
            }
            i++
        }
        val ans = ArrayList<MutableList<Int>>()
        for (x in 2..n / 2) {
            val y = n - x
            if (isPrime[x] && isPrime[y]) ans.add(mutableListOf(x, y))
        }
        return ans
    }
}
