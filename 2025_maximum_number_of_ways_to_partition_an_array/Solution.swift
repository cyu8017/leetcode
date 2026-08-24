// LeetCode 2025 - Maximum Number of Ways to Partition an Array
// https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/

class Solution {
    func waysToPartition(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var pref = [Int](repeating: 0, count: n)
        pref[0] = nums[0]
        for i in 1..<n { pref[i] = pref[i - 1] + nums[i] }
        let total = pref[n - 1]
        var right = [Int: Int]()
        var left = [Int: Int]()
        for i in 0..<(n - 1) { right[pref[i], default: 0] += 1 }
        var ans = 0
        if total % 2 == 0 { ans = right[total / 2, default: 0] }
        for i in 0..<n {
            let diff = k - nums[i]
            let newTotal = total + diff
            var cur = 0
            if newTotal % 2 == 0 {
                let half = newTotal / 2
                cur = left[half, default: 0] + right[half - diff, default: 0]
            }
            ans = max(ans, cur)
            if i < n - 1 {
                left[pref[i], default: 0] += 1
                right[pref[i]]! -= 1
            }
        }
        return ans
    }
}
