// LeetCode 3990 - Create Grid With Exactly K Paths II
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-ii/

class Solution {
    fun BitWidth(k: Int): Int {
        var w = 0
        while (k != 0) { ++w; k >>= 1; }
        return w
    }

    fun createGrid(k: Int): Array<String> {
        if (k <= 0) return arrayOfNulls<String>(0)
        var l = BitWidth(k)
        var m = 2 * l
        var n = l + 3
        var result = arrayOfNulls<String>(m)
        for (i in 0 until m) {
            var row = CharArray(n)
            for (j in 0 until n) { row[j] = '#' }
            result[i] = String(row)
        }
        for (i in 0 until l) {
            var r = 2 * i
            var row0 = result[r].toCharArray()
            var row1 = result[r + 1].toCharArray()
            row0[i] = row0[i + 1] = row1[i] = row1[i + 1] = '.'
            if ((k & (1  shl  i)) != 0) {
                for (c in i + 2 until n) { row0[c] = '.' }
            }
            result[r] = String(row0)
            result[r + 1] = String(row1)
        }
        for (r in 0 until m) {
            var row = result[r].toCharArray()
            row[n - 1] = '.'
            result[r] = String(row)
        }
        return result
    }
}
