// LeetCode 1424 - Diagonal Traverse II
// https://leetcode.com/problems/diagonal-traverse-ii/

class Solution {
    fun findDiagonalOrder(nums: List<List<Int>>): IntArray {
        val diagonals = HashMap<Int, ArrayList<Int>>()
        for (row in nums.indices) {
            for (col in nums[row].indices) {
                diagonals.getOrPut(row + col) { ArrayList() }.add(nums[row][col])
            }
        }
        val answer = ArrayList<Int>()
        for (key in diagonals.keys.sorted()) {
            val diag = diagonals[key]!!
            for (i in diag.size - 1 downTo 0) answer.add(diag[i])
        }
        return answer.toIntArray()
    }
}
