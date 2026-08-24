// LeetCode 3740 - Minimum Distance Between Three Equal Elements I
// https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/

class Solution {
    func minimumDistance(_ nums: [Int]) -> Int {
        var g = [Int: [Int]]()
        for i in 0..<nums.count {
            g[nums[i], default: []].append(i)
        }
        let inf = 1 << 30
        var ans = inf
        for ls in g.values {
            let m = ls.count
            if m >= 3 {
                for h in 0..<(m - 2) {
                    ans = min(ans, (ls[h + 2] - ls[h]) * 2)
                }
            }
        }
        return ans == inf ? -1 : ans
    }
}
