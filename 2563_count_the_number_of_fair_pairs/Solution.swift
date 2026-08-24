// LeetCode 2563 - Count the Number of Fair Pairs
// https://leetcode.com/problems/count-the-number-of-fair-pairs/

class Solution {
    func countFairPairs(_ nums: [Int], _ lower: Int, _ upper: Int) -> Int {
        let nums = nums.sorted()
        func count(_ x: Int) -> Int {
            var ans = 0, l = 0, r = nums.count - 1
            while l < r {
                if nums[l] + nums[r] <= x {
                    ans += r - l
                    l += 1
                } else {
                    r -= 1
                }
            }
            return ans
        }
        return count(upper) - count(lower - 1)
    }
}
