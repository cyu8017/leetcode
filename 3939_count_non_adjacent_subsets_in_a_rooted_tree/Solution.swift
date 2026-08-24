// LeetCode 3939 - Count Non Adjacent Subsets in a Rooted Tree
// https://leetcode.com/problems/count-non-adjacent-subsets-in-a-rooted-tree/


class Solution {
    func countNonAdjacentSubsets(_ parent: [Int], _ nums: [Int], _ k: Int) -> Int {
        let mod = 1_000_000_007
        let n = parent.count
        var children = Array(repeating: [Int](), count: n)
        for i in 1..<n { children[parent[i]].append(i) }
        var dp0 = Array(repeating: [Int](), count: n)
        var dp1 = Array(repeating: [Int](), count: n)
        for u in stride(from: n - 1, through: 0, by: -1) {
            var a = Array(repeating: 0, count: k)
            var b = Array(repeating: 0, count: k)
            a[0] = 1
            b[((nums[u] % k) + k) % k] = 1
            for v in children[u] {
                var na = Array(repeating: 0, count: k)
                var nb = Array(repeating: 0, count: k)
                for x in 0..<k {
                    for y in 0..<k {
                        let allChild = (dp0[v][y] + dp1[v][y]) % mod
                        na[(x + y) % k] = (na[(x + y) % k] + a[x] * allChild) % mod
                        nb[(x + y) % k] = (nb[(x + y) % k] + b[x] * dp0[v][y]) % mod
                    }
                }
                a = na
                b = nb
            }
            dp0[u] = a
            dp1[u] = b
        }
        var ans = (dp0[0][0] + dp1[0][0] - 1) % mod
        if ans < 0 { ans += mod }
        return ans
    }
}
