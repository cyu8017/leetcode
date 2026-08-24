// LeetCode 2305 - Fair Distribution of Cookies
// https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution {
    private lateinit var cookies: IntArray
    private lateinit var bags: IntArray
    private var ans = Int.MAX_VALUE

    fun distributeCookies(cookies: IntArray, k: Int): Int {
        this.cookies = cookies
        bags = IntArray(k)
        ans = Int.MAX_VALUE
        dfs(0)
        return ans
    }

    private fun dfs(i: Int) {
        if (i == cookies.size) {
            ans = minOf(ans, bags.max())
            return
        }
        val seen = HashSet<Int>()
        for (j in bags.indices) {
            if (!seen.add(bags[j])) continue
            bags[j] += cookies[i]
            if (bags[j] < ans) dfs(i + 1)
            bags[j] -= cookies[i]
            if (bags[j] == 0) break
        }
    }
}
