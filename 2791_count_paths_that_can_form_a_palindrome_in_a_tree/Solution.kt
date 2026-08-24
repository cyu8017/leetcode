// LeetCode 2791 - Count Paths That Can Form a Palindrome in a Tree
// https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/

class Solution {
    private var ans = 0L
    private lateinit var freq: HashMap<Int, Int>
    private lateinit var g: Array<ArrayList<Int>>
    private lateinit var s: String

    fun countPalindromePaths(parent: MutableList<Int>, s: String): Long {
        val n = parent.size
        this.s = s
        g = Array(n) { ArrayList() }
        for (i in 1 until n) g[parent[i]].add(i)
        freq = HashMap()
        freq[0] = 1
        ans = 0
        dfs(0, 0)
        return ans
    }

    private fun dfs(u: Int, mask: Int) {
        for (v in g[u]) {
            val nm = mask xor (1 shl (s[v] - 'a'))
            ans += freq.getOrDefault(nm, 0)
            for (b in 0 until 26) {
                ans += freq.getOrDefault(nm xor (1 shl b), 0)
            }
            freq[nm] = freq.getOrDefault(nm, 0) + 1
            dfs(v, nm)
        }
    }
}
