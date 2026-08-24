// LeetCode 3044 - Most Frequent Prime
// https://leetcode.com/problems/most-frequent-prime/

class Solution {
    private fun isPrime(n: Int): Boolean {
        if (n < 2) return false
        var i = 2
        while (i <= n / i) {
            if (n % i == 0) return false
            i++
        }
        return true
    }

    fun mostFrequentPrime(mat: Array<IntArray>): Int {
        val m = mat.size
        val n = mat[0].size
        val cnt = HashMap<Int, Int>()
        for (i in 0 until m) {
            for (j in 0 until n) {
                for (a in -1..1) {
                    for (b in -1..1) {
                        if (a == 0 && b == 0) continue
                        var x = i + a
                        var y = j + b
                        var v = mat[i][j]
                        while (x >= 0 && x < m && y >= 0 && y < n) {
                            v = v * 10 + mat[x][y]
                            if (isPrime(v)) {
                                cnt[v] = cnt.getOrDefault(v, 0) + 1
                            }
                            x += a
                            y += b
                        }
                    }
                }
            }
        }
        var ans = -1
        var mx = 0
        for ((key, value) in cnt) {
            if (mx < value || (mx == value && ans < key)) {
                mx = value
                ans = key
            }
        }
        return ans
    }
}
