// LeetCode 2983 - Palindrome Rearrangement Queries
// https://leetcode.com/problems/palindrome-rearrangement-queries/

class Solution {
    fun canMakePalindromeQueries(s0: String, queries: Array<IntArray>): MutableList<Boolean> {
        val n = s0.length
        val m = n / 2
        val tArr = s0.substring(m).toCharArray()
        var i = 0
        var j = tArr.size - 1
        while (i < j) {
            val tmp = tArr[i]
            tArr[i] = tArr[j]
            tArr[j] = tmp
            i++
            j--
        }
        val t = String(tArr)
        val s = s0.substring(0, m)

        val pre1 = Array(m + 1) { IntArray(26) }
        val pre2 = Array(m + 1) { IntArray(26) }
        val diff = IntArray(m + 1)
        for (ii in 1..m) {
            pre1[ii] = pre1[ii - 1].copyOf()
            pre2[ii] = pre2[ii - 1].copyOf()
            pre1[ii][s[ii - 1] - 'a']++
            pre2[ii][t[ii - 1] - 'a']++
            diff[ii] = diff[ii - 1] + if (s[ii - 1] == t[ii - 1]) 0 else 1
        }

        val ans = ArrayList<Boolean>(queries.size)
        for (qi in queries.indices) {
            val q = queries[qi]
            val a = q[0]
            val b = q[1]
            val c = n - 1 - q[3]
            val d = n - 1 - q[2]
            ans.add(
                if (a <= c) check(pre1, pre2, diff, a, b, c, d)
                else check(pre2, pre1, diff, c, d, a, b)
            )
        }
        return ans
    }

    private fun check(pre1: Array<IntArray>, pre2: Array<IntArray>, diff: IntArray, a: Int, b: Int, c: Int, d: Int): Boolean {
        if (diff[a] > 0 || diff[diff.size - 1] - diff[maxOf(b, d) + 1] > 0) return false
        if (d <= b) return eq(count(pre1, a, b), count(pre2, a, b))
        if (b < c) {
            return diff[c] - diff[b + 1] == 0 &&
                eq(count(pre1, a, b), count(pre2, a, b)) &&
                eq(count(pre1, c, d), count(pre2, c, d))
        }
        val cnt1 = sub(count(pre1, a, b), count(pre2, a, c - 1)) ?: return false
        val cnt2 = sub(count(pre2, c, d), count(pre1, b + 1, d)) ?: return false
        return eq(cnt1, cnt2)
    }

    private fun count(pre: Array<IntArray>, i: Int, j: Int): IntArray {
        val cnt = IntArray(26)
        for (k in 0 until 26) cnt[k] = pre[j + 1][k] - pre[i][k]
        return cnt
    }

    private fun sub(cnt1: IntArray, cnt2: IntArray): IntArray? {
        val cnt = IntArray(26)
        for (i in 0 until 26) {
            cnt[i] = cnt1[i] - cnt2[i]
            if (cnt[i] < 0) return null
        }
        return cnt
    }

    private fun eq(a: IntArray, b: IntArray): Boolean {
        for (i in 0 until 26) if (a[i] != b[i]) return false
        return true
    }
}
