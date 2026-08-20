// LeetCode 1512 - Number of Good Pairs
// https://leetcode.com/problems/number-of-good-pairs/

class Solution {
    func numIdenticalPairs(_ nums: [Int]) -> Int {
        var counts = [Int: Int]()
        for num in nums { counts[num, default: 0] += 1 }
        return counts.values.reduce(0) { $0 + $1 * ($1 - 1) / 2 }
    }
}
