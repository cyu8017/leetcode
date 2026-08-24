// LeetCode 3737 - Count Subarrays With Majority Element I
// https://leetcode.com/problems/count-subarrays-with-majority-element-i/

class Solution {
    func countMajoritySubarrays(_ nums: [Int], _ target: Int) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            var cnt = 0
            for j in i..<n {
                if nums[j] == target { cnt += 1 }
                if cnt * 2 > j - i + 1 { ans += 1 }
            }
        }
        return ans
    }
}
