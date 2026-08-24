// LeetCode 3347 - Maximum Frequency of an Element After Performing Operations II
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

class Solution {
    func maxFrequency(_ nums: [Int], _ k: Int, _ numOperations: Int) -> Int {
        let nums = nums.sorted()
        var freq = [Int: Int]()
        for x in nums { freq[x, default: 0] += 1 }
        var ans = 1
        var seen = Set<Int>()
        var candidates = [Int]()
        for x in nums {
            for t in [x - k, x, x + k] {
                if seen.insert(t).inserted { candidates.append(t) }
            }
        }
        for t in candidates {
            let lo = lowerBound(nums, t - k)
            let hi = upperBound(nums, t + k)
            let can = hi - lo
            let f = freq[t, default: 0]
            ans = max(ans, min(can, f + numOperations))
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
    private func upperBound(_ a: [Int], _ x: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] <= x { lo = mid + 1 } else { hi = mid }
        }
        return lo
    }

}
