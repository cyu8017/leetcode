// LeetCode 2799 - Count Complete Subarrays in an Array
// https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution {
    func countCompleteSubarrays(_ nums: [Int]) -> Int {
        let need = Set(nums).count
        var ans = 0
        let n = nums.count
        for i in 0..<n {
            var seen = Set<Int>()
            for j in i..<n {
                seen.insert(nums[j])
                if seen.count == need {
                    ans += n - j
                    break
                }
            }
        }
        return ans
    }
}
