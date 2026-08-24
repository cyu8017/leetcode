// LeetCode 3761 - Minimum Absolute Distance Between Mirror Pairs
// https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/

class Solution {
    func minMirrorPairDistance(_ nums: [Int]) -> Int {
        let n = nums.count
        var pos = [Int: Int]()
        var ans = n + 1
        for i in 0..<n {
            if let p = pos[nums[i]] { ans = min(ans, i - p) }
            pos[reverse(nums[i])] = i
        }
        return ans > n ? -1 : ans
    }

    private func reverse(_ x: Int) -> Int {
        var x = x, y = 0
        while x > 0 {
            y = y * 10 + x % 10
            x /= 10
        }
        return y
    }
}
