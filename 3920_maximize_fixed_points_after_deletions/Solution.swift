// LeetCode 3920 - Maximize Fixed Points After Deletions
// https://leetcode.com/problems/maximize-fixed-points-after-deletions/

class Solution {
    func maxFixedPoints(_ nums: [Int]) -> Int {
        var tails = [Int]()
        for i in 0..<nums.count {
            if i < nums[i] { continue }
            let d = i - nums[i]
            var lo = 0, hi = tails.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if tails[mid] < d { lo = mid + 1 }
                else { hi = mid }
            }
            if lo == tails.count { tails.append(d) }
            else { tails[lo] = d }
        }
        return tails.count
    }
}
