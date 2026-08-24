// LeetCode 3107 - Minimum Operations to Make Median of Array Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/

class Solution {
    func minOperationsToMakeMedianK(_ nums: [Int], _ k: Int) -> Int {
        let a = nums.sorted()
        let n = a.count, m = n >> 1
        var ans = abs(a[m] - k)
        if a[m] > k {
            var i = m - 1
            while i >= 0 && a[i] > k {
                ans += a[i] - k
                i -= 1
            }
        } else {
            var i = m + 1
            while i < n && a[i] < k {
                ans += k - a[i]
                i += 1
            }
        }
        return ans
    }
}
