// LeetCode 1187 - Make Array Strictly Increasing
// https://leetcode.com/problems/make-array-strictly-increasing/

class Solution {
    func makeArrayIncreasing(_ arr1: [Int], _ arr2: [Int]) -> Int {
        let sorted = Array(Set(arr2)).sorted()
        var dp: [Int: Int] = [-1: 0]
        for num in arr1 {
            var next: [Int: Int] = [:]
            for (prev, ops) in dp {
                if num > prev {
                    next[num] = min(next[num] ?? Int.max, ops)
                }
                let idx = upperBound(sorted, prev)
                if idx < sorted.count {
                    let chosen = sorted[idx]
                    next[chosen] = min(next[chosen] ?? Int.max, ops + 1)
                }
            }
            dp = next
            if dp.isEmpty { return -1 }
        }
        return dp.values.min() ?? -1
    }

    private func upperBound(_ a: [Int], _ target: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] <= target { lo = mid + 1 } else { hi = mid }
        }
        return lo
    }
}
