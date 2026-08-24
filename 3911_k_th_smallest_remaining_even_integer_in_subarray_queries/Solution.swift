// LeetCode 3911 - K-th Smallest Remaining Even Integer in Subarray Queries
// https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/

class Solution {
    func kthSmallestEven(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        let n = nums.count
        var evenPrefix = [Int](repeating: 0, count: n + 1)
        for i in 0..<n {
            evenPrefix[i + 1] = evenPrefix[i] + (nums[i] % 2 == 0 ? 1 : 0)
        }
        var ans = [Int](repeating: 0, count: queries.count)
        for qi in 0..<queries.count {
            let l = queries[qi][0], r = queries[qi][1]
            let k = queries[qi][2]
            var lo = 1, hi = k + (r - l + 1)
            while lo < hi {
                let mid = (lo + hi) / 2
                var pos = upperBound(nums, 2 * mid)
                if pos > r + 1 { pos = r + 1 }
                var removed = 0
                if pos > l { removed = evenPrefix[pos] - evenPrefix[l] }
                if mid - removed >= k { hi = mid }
                else { lo = mid + 1 }
            }
            ans[qi] = 2 * lo
        }
        return ans
    }

    private func upperBound(_ a: [Int], _ x: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] <= x { lo = mid + 1 }
            else { hi = mid }
        }
        return lo
    }
}
