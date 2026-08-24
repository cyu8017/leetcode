// LeetCode 2485 - Find the Pivot Integer
// https://leetcode.com/problems/find-the-pivot-integer/

class Solution {
    fun pivotInteger(n: Int): Int {
            var total: Int = n * (n + 1) / 2
            var sum: Int = 0
            var x: Int = 1
    while (x <= n) {
    
                sum +=x
                if (sum == total - sum + x) return x
    
    x = x + 1
    }
            return -1
    }
}
