// LeetCode 1984 - Minimum Difference Between Highest and Lowest of K Scores
// https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

class Solution {
    func minimumDifference(_ nums: [Int], _ k: Int) -> Int {
        let nums = nums.sorted()
        var ans = Int.max
        for i in 0...(nums.count - k) {
            ans = min(ans, nums[i + k - 1] - nums[i])
        }
        return ans
    }
}
