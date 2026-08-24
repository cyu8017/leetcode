// LeetCode 2500 - Delete Greatest Value in Each Row
// https://leetcode.com/problems/delete-greatest-value-in-each-row/

class Solution {
    fun deleteGreatestValue(grid: Array<IntArray>): Int {
            for (row in grid) row.sort()
            var ans: Int = 0
            var n: Int = grid[0].size
            var c: Int = 0
    while (c < n) {
    
                var mx: Int = 0
                for (row in grid) if (row[c] > mx) mx = row[c]
                ans +=mx
    
    c = c + 1
    }
            return ans
    }
}
