// LeetCode 0740 - Delete and Earn
// https://leetcode.com/problems/delete-and-earn/

class Solution {
    func deleteAndEarn(_ nums: [Int]) -> Int {
        let mx = nums.max()!
        var points = Array(repeating: 0, count: mx + 1)
        for n in nums { points[n] += n }
        var take = 0, skip = 0
        for p in points {
            let nxtTake = skip + p
            skip = max(skip, take)
            take = nxtTake
        }
        return max(take, skip)
    }
}
