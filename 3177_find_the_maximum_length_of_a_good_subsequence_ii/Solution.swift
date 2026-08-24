// LeetCode 3177 - Find the Maximum Length of a Good Subsequence II
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/

class Solution {
    func maximumLength(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var f = Array(repeating: Array(repeating: 0, count: k + 1), count: n)
        var mp = Array(repeating: [Int: Int](), count: k + 1)
        var g = Array(repeating: [0, 0, 0], count: k + 1)
        var ans = 0
        for i in 0..<n {
            for h in 0...k {
                f[i][h] = mp[h][nums[i], default: 0]
                if h > 0 {
                    if g[h - 1][0] != nums[i] {
                        f[i][h] = max(f[i][h], g[h - 1][1])
                    } else {
                        f[i][h] = max(f[i][h], g[h - 1][2])
                    }
                }
                f[i][h] += 1
                mp[h][nums[i]] = max(mp[h][nums[i], default: 0], f[i][h])
                if g[h][0] != nums[i] {
                    if f[i][h] >= g[h][1] {
                        g[h][2] = g[h][1]
                        g[h][1] = f[i][h]
                        g[h][0] = nums[i]
                    } else if f[i][h] > g[h][2] {
                        g[h][2] = f[i][h]
                    }
                } else if f[i][h] > g[h][1] {
                    g[h][1] = f[i][h]
                }
                ans = max(ans, f[i][h])
            }
        }
        return ans
    }
}
