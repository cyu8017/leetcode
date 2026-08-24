// LeetCode 2482 - Difference Between Ones and Zeros in Row and Column
// https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

class Solution {
    fun onesMinusZeros(grid: Array<IntArray>): Array<IntArray> {
            var m: Int = grid.size
            var n: Int = grid[0].size
            var row: IntArray = IntArray(m)
            var col: IntArray = IntArray(n)
            var i: Int = 0
    while (i < m) {
    
                var j: Int = 0
while (j < n) {

                    row[i] +=grid[i][j]
                    col[j] +=grid[i][j]
j = j + 1
}
    
    i = i + 1
    }
            var ans: Array<IntArray> = Array(m) { IntArray(n) }
            var i: Int = 0
    while (i < m) {
    
                var j: Int = 0
while (j < n) {

                    ans[i][j] = row[i] + col[j] - (m - row[i]) - (n - col[j])
j = j + 1
}
    
    i = i + 1
    }
            return ans
    }
}
