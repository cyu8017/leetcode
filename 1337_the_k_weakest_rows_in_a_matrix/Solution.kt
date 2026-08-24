// LeetCode 1337 - The K Weakest Rows in a Matrix
// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution {
    fun kWeakestRows(mat: Array<IntArray>, k: Int): IntArray {
        return mat.indices
            .sortedWith(compareBy({ mat[it].sum() }, { it }))
            .take(k)
            .toIntArray()
    }
}
