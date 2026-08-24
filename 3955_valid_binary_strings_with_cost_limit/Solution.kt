// LeetCode 3955 - Valid Binary Strings With Cost Limit
// https://leetcode.com/problems/valid-binary-strings-with-cost-limit/

class Solution {
    fun generateValidStrings(n: Int, k: Int): MutableList<String> {
        var ans = ArrayList<String>()
        var path = StringBuilder()
        dfs(0, 0, n, k, path, ans)
        return ans
    }

    private fun dfs(i: Int, tot: Int, n: Int, k: Int, path: StringBuilder, ans: MutableList<String>) {
        if (i >= n) {
            ans.add(path.toString())
            return
        }
        path.append('0')
        dfs(i + 1, tot, n, k, path, ans)
        path.deleteCharAt(path.length - 1)
        if ((path.length == 0 || path[path.length - 1] == '0') && tot + i <= k) {
            path.append('1')
            dfs(i + 1, tot + i, n, k, path, ans)
            path.deleteCharAt(path.length - 1)
        }
    }
}
