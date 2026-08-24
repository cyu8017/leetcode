// LeetCode 2817 - Minimum Absolute Difference Between Elements With Constraint
// https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

class Solution {
    func minAbsoluteDifference(_ nums: [Int], _ x: Int) -> Int {
        if x == 0 {
            var ans0 = Int.max
            for i in 1..<nums.count { ans0 = min(ans0, abs(nums[i] - nums[i - 1])) }
            return ans0
        }
        var ans = Int.max
        var arr: [Int] = []
        for i in x..<nums.count {
            insert(&arr, nums[i - x])
            let cur = nums[i]
            let idx = lowerBound(arr, cur)
            if idx < arr.count { ans = min(ans, arr[idx] - cur) }
            if idx > 0 { ans = min(ans, cur - arr[idx - 1]) }
        }
        return ans
    }

    private func insert(_ a: inout [Int], _ x: Int) {
        let i = lowerBound(a, x)
        a.insert(x, at: i)
    }

    private func lowerBound(_ a: [Int], _ x: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] < x { lo = mid + 1 } else { hi = mid }
        }
        return lo
    }
}
