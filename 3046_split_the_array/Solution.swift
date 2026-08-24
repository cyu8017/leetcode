// LeetCode 3046 - Split the Array
// https://leetcode.com/problems/split-the-array/

class Solution {
    func isPossibleToSplit(_ nums: [Int]) -> Bool {
        var cnt = Array(repeating: 0, count: 101)
        for x in nums {
            cnt[x] += 1
            if cnt[x] >= 3 { return false }
        }
        return true
    }
}
