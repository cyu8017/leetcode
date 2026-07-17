// LeetCode 1712 - Ways to Split Array Into Three Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

class Solution {
    func waysToSplit(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        let n = nums.count
        var prefix = [Int](repeating: 0, count: n)
        var total = 0
        for i in 0..<n {
            total += nums[i]
            prefix[i] = total
        }

        func lowerBound(_ target: Int, _ start: Int, _ end: Int) -> Int {
            var lo = start
            var hi = end
            while lo < hi {
                let mid = (lo + hi) / 2
                if prefix[mid] < target {
                    lo = mid + 1
                } else {
                    hi = mid
                }
            }
            return lo
        }

        func upperBound(_ target: Int, _ start: Int, _ end: Int) -> Int {
            var lo = start
            var hi = end
            while lo < hi {
                let mid = (lo + hi) / 2
                if prefix[mid] <= target {
                    lo = mid + 1
                } else {
                    hi = mid
                }
            }
            return lo
        }

        var ans = 0
        for i in 0..<(n - 2) {
            let left = prefix[i]
            let lo = lowerBound(2 * left, i + 1, n - 1)
            let hi = upperBound((total + left) / 2, lo, n - 1)
            ans = (ans + hi - lo) % mod
        }
        return ans
    }
}
