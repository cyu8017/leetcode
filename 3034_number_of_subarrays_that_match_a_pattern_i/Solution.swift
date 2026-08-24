// LeetCode 3034 - Number of Subarrays That Match a Pattern I
// https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/

class Solution {
    func countMatchingSubarrays(_ nums: [Int], _ pattern: [Int]) -> Int {
        let n = nums.count, m = pattern.count
        var ans = 0
        for i in 0..<(n - m) {
            var ok = true
            for k in 0..<m {
                if f(nums[i + k], nums[i + k + 1]) != pattern[k] {
                    ok = false
                    break
                }
            }
            if ok { ans += 1 }
        }
        return ans
    }

    private func f(_ a: Int, _ b: Int) -> Int {
        if a == b { return 0 }
        return a < b ? 1 : -1
    }
}
