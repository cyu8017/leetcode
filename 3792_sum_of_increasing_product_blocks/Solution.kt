// LeetCode 3792 - Sum Of Increasing Product Blocks
// https://leetcode.com/problems/sum-of-increasing-product-blocks/

class Solution {
    fun sumOfBlocks(n: Int): Int {
        val MOD = 1000000007
        var ans = 0
        var k = 1
        for (i in 1 ..n) {
            var x = 1
            for (j in k until k + i) { x = (x * j % MOD) }
            ans = (ans + x) % MOD
            k += i
        }
        return ans
    }
}
