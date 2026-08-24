// LeetCode 0910 - Smallest Range II
// https://leetcode.com/problems/smallest-range-ii/

class Solution {
    func smallestRangeII(_ nums: [Int], _ k: Int) -> Int {
        let a = nums.sorted()
        var ans = a.last! - a[0]
        for i in 0..<(a.count - 1) {
            let lo = min(a[0] + k, a[i + 1] - k)
            let hi = max(a.last! - k, a[i] + k)
            ans = min(ans, hi - lo)
        }
        return ans
    }
}
