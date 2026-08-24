// LeetCode 2913 - Subarrays Distinct Element Sum of Squares I
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

class Solution {
    func sumCounts(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            var seen = Set<Int>()
            for j in i..<n {
                seen.insert(nums[j])
                ans += seen.count * seen.count
            }
        }
        return ans
    }
}
