// LeetCode 3073 - Maximum Increasing Triplet Value
// https://leetcode.com/problems/maximum-increasing-triplet-value/

class Solution {
    func maximumTripletValue(_ nums: [Int]) -> Int {
        let n = nums.count
        var right = Array(repeating: 0, count: n)
        right[n - 1] = nums[n - 1]
        for i in stride(from: n - 2, through: 0, by: -1) {
            right[i] = max(nums[i], right[i + 1])
        }
        var sorted: [Int] = [nums[0]]
        var ans = 0
        for j in 1..<(n - 1) {
            if right[j + 1] > nums[j] {
                var lo = 0, hi = sorted.count
                while lo < hi {
                    let mid = (lo + hi) / 2
                    if sorted[mid] < nums[j] { lo = mid + 1 }
                    else { hi = mid }
                }
                if lo > 0 {
                    ans = max(ans, sorted[lo - 1] - nums[j] + right[j + 1])
                }
            }
            var lo = 0, hi = sorted.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if sorted[mid] < nums[j] { lo = mid + 1 }
                else { hi = mid }
            }
            if lo == sorted.count || sorted[lo] != nums[j] {
                sorted.insert(nums[j], at: lo)
            }
        }
        return ans
    }
}
