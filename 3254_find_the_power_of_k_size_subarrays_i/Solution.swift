// LeetCode 3254 - Find the Power of K-Size Subarrays I
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

class Solution {
    func resultsArray(_ nums: [Int], _ k: Int) -> [Int] {
        let n = nums.count
        var ans = Array(repeating: 0, count: n - k + 1)
        for i in 0...(n - k) {
            var ok = true
            if k >= 2 {
                for j in (i + 1)..<(i + k) where nums[j] != nums[j - 1] + 1 {
                    ok = false
                    break
                }
            }
            ans[i] = ok ? nums[i + k - 1] : -1
        }
        return ans
    }
}
