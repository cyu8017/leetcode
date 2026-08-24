// LeetCode 2428 - Maximum Sum of an Hourglass
// https://leetcode.com/problems/maximum-sum-of-an-hourglass/

class Solution {
    fun maxSum(grid: Array<IntArray>): Int {
            var m: Int = grid.size
            var n: Int = grid[0].size
            var ans: Int = 0
            var i: Int = 0
    while (i + 2 < m) {
    
                var j: Int = 0
while (j + 2 < n) {

                    int s = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
                          + grid[i + 1][j + 1]
                          + grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                    ans = maxOf(ans, s)
j = j + 1
}
    
    i = i + 1
    }
            return ans
    }
}
