// LeetCode 1569 - Number of Ways to Reorder Array to Get Same BST
// https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

class Solution {
    func numOfWays(_ nums: [Int]) -> Int {
        let MOD = 1_000_000_007
        let n = nums.count
        var choose = Array(repeating: Array(repeating: 0, count: n + 1), count: n + 1)
        for i in 0...n {
            choose[i][0] = 1
            choose[i][i] = 1
            if i >= 2 {
                for j in 1..<i {
                    choose[i][j] = (choose[i - 1][j - 1] + choose[i - 1][j]) % MOD
                }
            }
        }
        func ways(_ values: [Int]) -> Int {
            if values.count < 3 { return 1 }
            let left = values.dropFirst().filter { $0 < values[0] }
            let right = values.dropFirst().filter { $0 > values[0] }
            return choose[values.count - 1][left.count] * ways(Array(left)) % MOD * ways(Array(right)) % MOD
        }
        return (ways(nums) - 1 + MOD) % MOD
    }
}
