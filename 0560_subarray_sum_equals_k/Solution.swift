// LeetCode 0560 - Subarray Sum Equals K
// https://leetcode.com/problems/subarray-sum-equals-k/

class Solution {
    func subarraySum(_ nums: [Int], _ k: Int) -> Int {
        var counts = [0: 1]
        var prefix = 0
        var answer = 0
        for num in nums {
            prefix += num
            answer += counts[prefix - k, default: 0]
            counts[prefix, default: 0] += 1
        }
        return answer
    }
}
