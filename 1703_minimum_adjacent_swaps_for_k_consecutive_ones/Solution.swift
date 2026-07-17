// LeetCode 1703 - Minimum Adjacent Swaps for K Consecutive Ones
// https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/

class Solution {
    func minMoves(_ nums: [Int], _ k: Int) -> Int {
        var adjusted = [Int]()
        for (i, v) in nums.enumerated() where v == 1 {
            adjusted.append(i - adjusted.count)
        }
        let m = adjusted.count
        var prefix = [Int](repeating: 0, count: m + 1)
        for i in 0..<m {
            prefix[i + 1] = prefix[i] + adjusted[i]
        }
        var best = Int.max
        for left in 0...(m - k) {
            let right = left + k
            let mid = left + k / 2
            let median = adjusted[mid]
            var cost = median * (mid - left) - (prefix[mid] - prefix[left])
            cost += (prefix[right] - prefix[mid + 1]) - median * (right - mid - 1)
            best = min(best, cost)
        }
        return best
    }
}
