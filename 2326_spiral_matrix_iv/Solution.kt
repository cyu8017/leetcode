// LeetCode 2326 - Spiral Matrix IV
// https://leetcode.com/problems/spiral-matrix-iv/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun spiralMatrix(m: Int, n: Int, head: ListNode?): Array<IntArray> {
        val ans = Array(m) { IntArray(n) { -1 } }
        val dirs = arrayOf(intArrayOf(0, 1), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(-1, 0))
        var r = 0; var c = 0; var d = 0
        var cur = head
        while (cur != null) {
            ans[r][c] = cur.`val`
            cur = cur.next
            var nr = r + dirs[d][0]
            var nc = c + dirs[d][1]
            if (nr !in 0 until m || nc !in 0 until n || ans[nr][nc] != -1) {
                d = (d + 1) % 4
                nr = r + dirs[d][0]
                nc = c + dirs[d][1]
            }
            r = nr
            c = nc
        }
        return ans
    }
}
