// LeetCode 3144 - Minimum Substring Partition of Equal Character Frequency
// https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/

class Solution {
    private var s: String? = null
    private var n: Int = 0
    private var memo: IntArray? = null

    private fun dfs(i: Int): Int {
        if (i >= n) return 0
        if (memo[i] != -1) return memo[i]
        var cnt = IntArray(26)
        var freq = HashMap<Int, Int>()
        memo[i] = n - i
        for (j in i until n) {
            var k = s[j] - 'a'
            if (cnt[k] > 0) {
                var c = cnt[k]
                var nv = freq[c] - 1
                if (nv == 0) freq.remove(c)
                else freq[c] = nv
            }
            cnt[k]++
            freq[cnt[k]] = freq.getOrDefault(cnt[k], 0) + 1
            if (freq.size == 1) {
                memo[i] = minOf(memo[i], 1 + dfs(j + 1))
            }
        }
        return memo[i]
    }

    fun minimumSubstringsInPartition(s: String): Int {
        this.s = s
        this.n = s.length
        this.memo = IntArray(n)
        memo.fill(-1)
        return dfs(0)
    }
}
