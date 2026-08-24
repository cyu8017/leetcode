// LeetCode 3826 - Minimum Partition Score
// https://leetcode.com/problems/minimum-partition-score/

class Solution {
    private var prefix = [Int]()
    private var previous = [Int]()
    private var current = [Int]()
    private let INF = 1 << 62

    func minPartitionScore(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        prefix = [Int](repeating: 0, count: n + 1)
        for i in 0..<n { prefix[i + 1] = prefix[i] + nums[i] }
        previous = [Int](repeating: INF, count: n + 1)
        previous[0] = 0
        for parts in 1...k {
            current = [Int](repeating: INF, count: n + 1)
            compute(parts, n, parts - 1, n - 1)
            previous = current
        }
        return previous[n]
    }

    private func value(_ left: Int, _ right: Int) -> Int {
        let sum = prefix[right] - prefix[left]
        return sum * (sum + 1) / 2
    }

    private func compute(_ lo: Int, _ hi: Int, _ optLo: Int, _ optHi: Int) {
        if lo > hi { return }
        let mid = (lo + hi) / 2
        var bestIndex = -1
        let end = min(optHi, mid - 1)
        if optLo <= end {
            for split in optLo...end {
                if previous[split] == INF { continue }
                let candidate = previous[split] + value(split, mid)
                if candidate < current[mid] {
                    current[mid] = candidate
                    bestIndex = split
                }
            }
        }
        if bestIndex == -1 { bestIndex = optLo }
        compute(lo, mid - 1, optLo, bestIndex)
        compute(mid + 1, hi, bestIndex, optHi)
    }
}
