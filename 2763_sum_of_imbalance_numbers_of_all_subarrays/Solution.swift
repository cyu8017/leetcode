// LeetCode 2763 - Sum of Imbalance Numbers of All Subarrays
// https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/

class Solution {
    func sumImbalanceNumbers(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            var seen = Set<Int>()
            var sortedVals: [Int] = []
            var imbalance = 0
            for j in i..<n {
                let x = nums[j]
                if !seen.contains(x) {
                    seen.insert(x)
                    let idx = lowerBound(sortedVals, x)
                    let prev = idx > 0 ? sortedVals[idx - 1] : nil
                    let next = idx < sortedVals.count ? sortedVals[idx] : nil
                    if let p = prev, x - p != 1 { imbalance += 1 }
                    if let nx = next, nx - x != 1 { imbalance += 1 }
                    if let p = prev, let nx = next, nx - p > 1 { imbalance -= 1 }
                    sortedVals.insert(x, at: idx)
                }
                ans += imbalance
            }
        }
        return ans
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
