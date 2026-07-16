// LeetCode 0416 - Partition Equal Subset Sum
// https://leetcode.com/problems/partition-equal-subset-sum/

class Solution {
    func canPartition(_ nums: [Int]) -> Bool {
        let total = nums.reduce(0, +)
        if total % 2 != 0 {
            return false
        }

        let target = total / 2
        var possible: Set<Int> = [0]

        for value in nums {
            possible = possible.union(
                possible.compactMap { amount in
                    let updated = amount + value
                    return updated <= target ? updated : nil
                }
            )
            if possible.contains(target) {
                return true
            }
        }

        return possible.contains(target)
    }
}
