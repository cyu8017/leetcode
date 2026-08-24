// LeetCode 3470 - Permutations IV
// https://leetcode.com/problems/permutations-iv/

class Solution {
    func permute(_ n: Int, _ k: Int) -> [Int] {
        var fact = Array(repeating: 1, count: n + 1)
        if n >= 1 {
            for i in 1...n {
                fact[i] = fact[i - 1] * i
                if fact[i] > Int(1e18) { fact[i] = Int(1e18) + 1 }
            }
        }
        var used = Array(repeating: false, count: n + 1)
        var ans = [Int]()
        var k = k
        func dfs(_ pos: Int) -> Bool {
            if pos == n { return true }
            for x in 1...n {
                if used[x] { continue }
                if pos > 0 && (ans[pos - 1] % 2 == x % 2) { continue }
                let rem = n - pos - 1
                let cnt = fact[rem]
                if cnt >= k {
                    used[x] = true
                    ans.append(x)
                    if dfs(pos + 1) { return true }
                    ans.removeLast()
                    used[x] = false
                } else {
                    k -= cnt
                }
            }
            return false
        }
        if !dfs(0) { return [] }
        return ans
    }
}
