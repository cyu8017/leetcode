// LeetCode 0978 - Longest Turbulent Subarray
// https://leetcode.com/problems/longest-turbulent-subarray/

class Solution {
    func maxTurbulenceSize(_ arr: [Int]) -> Int {
        var ans = 1, cur = 1
        if arr.count > 1 {
            for i in 1..<arr.count {
                if arr[i] == arr[i - 1] {
                    cur = 1
                } else if i == 1 || (arr[i] - arr[i - 1]) * (arr[i - 1] - arr[i - 2]) < 0 {
                    cur += 1
                } else {
                    cur = 2
                }
                ans = max(ans, cur)
            }
        }
        return ans
    }
}
