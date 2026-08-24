// LeetCode 3154 - Find Number of Ways to Reach the K-th Stair
// https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/

class Solution {
    private var k = 0
    private var f: [Int: Int] = [:]

    func waysToReachStair(_ k: Int) -> Int {
        self.k = k
        self.f = [:]
        return dfs(1, 0, 0)
    }

    private func dfs(_ i: Int, _ j: Int, _ jump: Int) -> Int {
        if i > k + 1 { return 0 }
        let key = (i << 32) | (jump << 1) | j
        if let cached = f[key] { return cached }
        var ans = 0
        if i == k { ans += 1 }
        if i > 0 && j == 0 { ans += dfs(i - 1, 1, jump) }
        ans += dfs(i + (1 << jump), 0, jump + 1)
        f[key] = ans
        return ans
    }
}
