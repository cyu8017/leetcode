// LeetCode 3864 - Minimum Cost To Partition A Binary String
// https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/

class Solution {
    private var pre = [Int]()
    private var encCost = 0, flatCost = 0

    func minCost(_ s: String, _ encCost: Int, _ flatCost: Int) -> Int {
        let chars = Array(s)
        let n = chars.count
        self.encCost = encCost
        self.flatCost = flatCost
        pre = [Int](repeating: 0, count: n + 1)
        for i in 1...n { pre[i] = pre[i - 1] + Int(chars[i - 1].asciiValue! - 48) }
        return dfs(0, n)
    }

    private func dfs(_ l: Int, _ r: Int) -> Int {
        let x = pre[r] - pre[l]
        var res = x != 0 ? (r - l) * x * encCost : flatCost
        if (r - l) % 2 == 0 {
            let m = (l + r) / 2
            res = min(res, dfs(l, m) + dfs(m, r))
        }
        return res
    }
}
