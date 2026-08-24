// LeetCode 3792 - Sum Of Increasing Product Blocks
// https://leetcode.com/problems/sum-of-increasing-product-blocks/

class Solution {
    func sumOfBlocks(_ n: Int) -> Int {
        let MOD = 1_000_000_007
        var ans = 0, k = 1
        for i in 1...n {
            var x = 1
            for j in k..<(k + i) { x = x * j % MOD }
            ans = (ans + x) % MOD
            k += i
        }
        return ans
    }
}
