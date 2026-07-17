// LeetCode 1755 - Closest Subsequence Sum
// https://leetcode.com/problems/closest-subsequence-sum/

class Solution {
    func minAbsDifference(_ nums: [Int], _ goal: Int) -> Int {
        let n = nums.count
        let left = Array(nums[0..<(n / 2)])
        let right = Array(nums[(n / 2)...])

        func sums(_ arr: [Int]) -> [Int] {
            var vals = [0]
            vals.reserveCapacity(1 << arr.count)
            for x in arr {
                let size = vals.count
                for i in 0..<size {
                    vals.append(vals[i] + x)
                }
            }
            vals.sort()
            return vals
        }

        let a = sums(left)
        let b = sums(right)
        var best = Int.max
        var j = b.count - 1
        for x in a {
            while j > 0 && abs(x + b[j] - goal) >= abs(x + b[j - 1] - goal) {
                j -= 1
            }
            best = min(best, abs(x + b[j] - goal))
        }
        return best
    }
}
