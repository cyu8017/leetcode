// LeetCode 2824 - Count Pairs Whose Sum is Less than Target
// https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution {
    func countPairs(_ nums: [Int], _ target: Int) -> Int {
        var ans = 0
        for i in nums.indices {
            for j in (i + 1)..<nums.count where nums[i] + nums[j] < target { ans += 1 }
        }
        return ans
    }
}
