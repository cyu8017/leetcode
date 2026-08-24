// LeetCode 3346 - Maximum Frequency of an Element After Performing Operations I
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

class Solution {
    func maxFrequency(_ nums: [Int], _ k: Int, _ numOperations: Int) -> Int {
        let nums = nums.sorted()
        let n = nums.count
        var freq = [Int: Int]()
        for x in nums { freq[x, default: 0] += 1 }
        var ans = 1
        for (t, f) in freq {
            let lo = lowerBound(nums, t - k)
            let hi = upperBound(nums, t + k)
            let can = hi - lo
            let use = min(can, f + numOperations)
            if use > ans { ans = use }
        }
        var l = 0
        for r in 0..<n {
            while nums[r] - nums[l] > 2 * k { l += 1 }
            let window = min(r - l + 1, numOperations)
            if window > ans { ans = window }
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
