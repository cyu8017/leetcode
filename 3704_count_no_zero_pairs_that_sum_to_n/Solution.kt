// LeetCode 3704 - Count No-Zero Pairs That Sum to N
// https://leetcode.com/problems/count-no-zero-pairs-that-sum-to-n/

class Solution {
    fun countNoZeroPairs(n: Long): Long {
        val s = n.toString()
        val m = s.length
        val digits = IntArray(m + 1)
        for (i in 0 until m) digits[i] = s[m - 1 - i] - '0'

        var dp = Array(2) { Array(2) { LongArray(2) } }
        dp[0][1][1] = 1

        for (pos in 0..m) {
            val ndp = Array(2) { Array(2) { LongArray(2) } }
            val target = digits[pos]
            for (carry in 0..1) {
                for (aliveA in 0..1) {
                    for (aliveB in 0..1) {
                        val ways = dp[carry][aliveA][aliveB]
                        if (ways == 0L) continue
                        val A = Array(10) { IntArray(2) }
                        var aLen = 0
                        if (aliveA == 1) {
                            for (d in 1..9) {
                                A[aLen][0] = d
                                A[aLen][1] = 1
                                aLen++
                            }
                            if (pos > 0) {
                                A[aLen][0] = 0
                                A[aLen][1] = 0
                                aLen++
                            }
                        } else {
                            A[0][0] = 0
                            A[0][1] = 0
                            aLen = 1
                        }
                        val B = Array(10) { IntArray(2) }
                        var bLen = 0
                        if (aliveB == 1) {
                            for (d in 1..9) {
                                B[bLen][0] = d
                                B[bLen][1] = 1
                                bLen++
                            }
                            if (pos > 0) {
                                B[bLen][0] = 0
                                B[bLen][1] = 0
                                bLen++
                            }
                        } else {
                            B[0][0] = 0
                            B[0][1] = 0
                            bLen = 1
                        }
                        for (ai in 0 until aLen) {
                            val da = A[ai][0]
                            val na = A[ai][1]
                            for (bi in 0 until bLen) {
                                val db = B[bi][0]
                                val nb = B[bi][1]
                                val sum = da + db + carry
                                if (sum % 10 != target) continue
                                val ncarry = sum / 10
                                ndp[ncarry][na][nb] += ways
                            }
                        }
                    }
                }
            }
            for (c in 0..1) for (a in 0..1) for (b in 0..1) dp[c][a][b] = ndp[c][a][b]
        }
        return dp[0][0][0]
    }
}
