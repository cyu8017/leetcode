// LeetCode 3577 - Count the Number of Computer Unlocking Permutations
// https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

class Solution {
    func countPermutations(_ complexity: [Int]) -> Int {
        let mod = 1_000_000_007
        var ans = 1
        if complexity.count > 1 {
            for i in 1..<complexity.count {
                if complexity[i] <= complexity[0] { return 0 }
                ans = ans * i % mod
            }
        }
        return ans
    }
}
