// LeetCode 3109 - Find the Index of Permutation
// https://leetcode.com/problems/find-the-index-of-permutation/

private class BIT {
    let n: Int
    var c: [Int]
    init(_ n: Int) {
        self.n = n
        self.c = Array(repeating: 0, count: n + 1)
    }
    func update(_ x: Int, _ delta: Int) {
        var i = x
        while i <= n {
            c[i] += delta
            i += i & -i
        }
    }
    func query(_ x: Int) -> Int {
        var i = x, s = 0
        while i > 0 {
            s += c[i]
            i -= i & -i
        }
        return s
    }
}

class Solution {
    func getPermutationIndex(_ perm: [Int]) -> Int {
        let MOD = 1_000_000_007
        let n = perm.count
        let tree = BIT(n + 1)
        var f = Array(repeating: 0, count: n)
        f[0] = 1
        for i in 1..<n { f[i] = f[i - 1] * i % MOD }
        var ans = 0
        for i in 0..<n {
            let x = perm[i]
            let cnt = x - 1 - tree.query(x)
            ans = (ans + cnt * f[n - 1 - i]) % MOD
            tree.update(x, 1)
        }
        return ans
    }
}
