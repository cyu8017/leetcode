// LeetCode 2808 - Minimum Seconds to Equalize a Circular Array
// https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/

class Solution {
    func minimumSeconds(_ nums: [Int]) -> Int {
        let n = nums.count
        var pos: [Int: [Int]] = [:]
        for i in 0..<n { pos[nums[i], default: []].append(i) }
        var ans = n
        for p in pos.values {
            var maxGap = 0
            for i in p.indices {
                let gap = i + 1 < p.count ? p[i + 1] - p[i] : p[0] + n - p[i]
                maxGap = max(maxGap, gap / 2)
            }
            ans = min(ans, maxGap)
        }
        return ans
    }
}
