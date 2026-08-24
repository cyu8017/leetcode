// LeetCode 2638 - Count the Number of K-Free Subsets
// https://leetcode.com/problems/count-the-number-of-k-free-subsets/

class Solution {
    func countTheNumOfKFreeSubsets(_ nums: [Int], _ k: Int) -> Int {
        var nums = nums.sorted()
        var groups: [Int: [Int]] = [:]
        for x in nums { groups[x % k, default: []].append(x) }
        var ans = 1
        for g in groups.values {
            var prevVal = -1
            var prevTake = 0
            var prevSkip = 1
            for v in g {
                let skip = prevTake + prevSkip
                let take = prevVal + k == v ? prevSkip : prevTake + prevSkip
                prevTake = take
                prevSkip = skip
                prevVal = v
            }
            ans *= prevTake + prevSkip
        }
        return ans
    }
}
