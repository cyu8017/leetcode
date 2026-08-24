// LeetCode 3827 - Count Monobit Integers
// https://leetcode.com/problems/count-monobit-integers/

class Solution {
    fun countMonobit(n: Int): Int {
        var ans = 1
        var i = 1
        var x = 1
        while (x <= n) {
            ans++
            x += (1  shl  i)
            i++
        }
        return ans
    }
}
