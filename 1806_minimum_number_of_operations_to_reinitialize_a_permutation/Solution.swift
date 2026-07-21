// LeetCode 1806 - Minimum Number of Operations to Reinitialize a Permutation
// https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/

class Solution {
    func reinitializePermutation(_ n: Int) -> Int {
        var perm = Array(0..<n)
        let target = perm
        var operations = 0
        while true {
            var newPerm = Array(repeating: 0, count: n)
            for i in 0..<n {
                if i % 2 == 0 {
                    newPerm[i] = perm[i / 2]
                } else {
                    newPerm[i] = perm[n / 2 + (i - 1) / 2]
                }
            }
            perm = newPerm
            operations += 1
            if perm == target {
                return operations
            }
        }
    }
}
