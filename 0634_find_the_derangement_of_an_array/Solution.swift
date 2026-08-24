// LeetCode 0634 - Find the Derangement of An Array
// https://leetcode.com/problems/find-the-derangement-of-an-array/

class Solution {
    func findDerangement(_ n: Int) -> Int {
        let mod = 1_000_000_007
        if n == 1 { return 0 }
        var prev2 = 0
        var prev1 = 1
        if n >= 3 {
            for size in 3...n {
                let next = (size - 1) * (prev1 + prev2) % mod
                prev2 = prev1
                prev1 = next
            }
        }
        return prev1
    }
}
