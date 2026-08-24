// LeetCode 3850 - Count Sequences To K
// https://leetcode.com/problems/count-sequences-to-k/

class Solution {
    private var nums = [Int]()
    private var k = 0
    private var f = [String: Int]()

    func countSequences(_ nums: [Int], _ k: Int) -> Int {
        self.nums = nums
        self.k = k
        f = [:]
        return dfs(0, 1, 1)
    }

    private func gcd(_ a: Int, _ b: Int) -> Int {
        var a = a, b = b
        while b != 0 {
            let t = a % b
            a = b
            b = t
        }
        return a
    }

    private func dfs(_ i: Int, _ p: Int, _ q: Int) -> Int {
        if i == nums.count { return (p == k && q == 1) ? 1 : 0 }
        let key = "\(i),\(p),\(q)"
        if let cached = f[key] { return cached }
        var res = dfs(i + 1, p, q)
        let x = nums[i]
        let g1 = gcd(p * x, q)
        res += dfs(i + 1, (p * x) / g1, q / g1)
        let g2 = gcd(p, q * x)
        res += dfs(i + 1, p / g2, (q * x) / g2)
        f[key] = res
        return res
    }
}
