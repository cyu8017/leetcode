// LeetCode 2963 - Count the Number of Good Partitions
// https://leetcode.com/problems/count-the-number-of-good-partitions/

class Solution {
    func numberOfGoodPartitions(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        var last: [Int: Int] = [:]
        for i in 0..<nums.count { last[nums[i]] = i }
        var ans = 1, end = 0
        for i in 0..<nums.count {
            end = max(end, last[nums[i]]!)
            if i == end && i != nums.count - 1 {
                ans = ans * 2 % mod
            }
        }
        return ans
    }
}
