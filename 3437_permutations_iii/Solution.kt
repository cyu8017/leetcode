// LeetCode 3437 - Permutations III
// https://leetcode.com/problems/permutations-iii/

class Solution {
    fun permute(n: Int): Array<IntArray> {
        var ans = ArrayList<IntArray>()
        var used = BooleanArray(n + 1)
        var cur = ArrayList<Int>()
        dfs(n, used, cur, ans)
        var res = IntArray(ans.size)[]
        for (i in 0 until ans.size) { res[i] = ans[i] }
        return res
    }

    private fun dfs(n: Int, used: BooleanArray, cur: MutableList<Int>, ans: MutableList<IntArray>) {
        if (cur.size == n) {
            var a = IntArray(n)
            for (i in 0 until n) { a[i] = cur[i] }
            ans.add(a)
            return
        }
        for (i in 1 .. n) {
            if (used[i]) continue
            if (!cur.isEmpty() && (cur[cur.size - 1] % 2 == i % 2)) continue
            used[i] = true
            cur.add(i)
            dfs(n, used, cur, ans)
            cur.remove(cur.size - 1)
            used[i] = false
        }
    }
}
