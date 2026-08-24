// LeetCode 3720 - Lexicographically Smallest Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically_smallest_permutation_greater_than_target/

class Solution {
    private var cnt: IntArray? = null
    private var ans: CharArray? = null
    private var target: String? = null
    private var n: Int = 0

    fun lexGreaterPermutation(s: String, target: String): String {
        cnt = IntArray(26)
        for (c in s.toCharArray()) { cnt[c - 'a']++ }
        n = s.length
        this.target = target
        ans = CharArray(n)
        if (dfs(0, false)) return String(ans)
        return ""
    }

    private fun dfs(pos: Int, greater: Boolean): Boolean {
        if (pos == n) return greater
        var start = if (greater) 0 else (target[pos] - 'a')
        for (c in start until 26) {
            if (cnt[c] == 0) continue
            cnt[c]--
            ans[pos] = ('a' + c).toInt().toChar()
            var ng = greater || c > (target[pos] - 'a')
            if (dfs(pos + 1, ng)) return true
            cnt[c]++
        }
        return false
    }
}
