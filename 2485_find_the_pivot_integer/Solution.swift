// LeetCode 2485 - Find the Pivot Integer
// https://leetcode.com/problems/find-the-pivot-integer/

class Solution {
    func pivotInteger(_ n: Int) -> Int {
        let total = n * (n + 1) / 2
        var sum = 0
        for x in 1...n {
            sum += x
            if sum == total - sum + x { return x }
        }
        return -1
    }
}
