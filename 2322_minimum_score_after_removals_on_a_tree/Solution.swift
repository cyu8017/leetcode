// LeetCode 2322 - Minimum Score After Removals on a Tree
// https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

class Solution {
    func minimumScore(_ nums: [Int], _ edges: [[Int]]) -> Int {
        let n = nums.count
        var g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        var xorv = [Int](repeating: 0, count: n)
        var inT = [Int](repeating: 0, count: n)
        var outT = [Int](repeating: 0, count: n)
        var time = 0
        func dfs(_ u: Int, _ p: Int) {
            inT[u] = time
            time += 1
            xorv[u] = nums[u]
            for v in g[u] where v != p {
                dfs(v, u)
                xorv[u] ^= xorv[v]
            }
            outT[u] = time
        }
        dfs(0, -1)
        func isAncestor(_ a: Int, _ b: Int) -> Bool {
            inT[a] <= inT[b] && outT[b] <= outT[a]
        }
        let total = xorv[0]
        var ans = Int.max
        if n >= 3 {
            for i in 1..<n {
                for j in (i + 1)..<n {
                    let a: Int, b: Int, c: Int
                    if isAncestor(i, j) {
                        a = xorv[j]; b = xorv[i] ^ xorv[j]; c = total ^ xorv[i]
                    } else if isAncestor(j, i) {
                        a = xorv[i]; b = xorv[j] ^ xorv[i]; c = total ^ xorv[j]
                    } else {
                        a = xorv[i]; b = xorv[j]; c = total ^ xorv[i] ^ xorv[j]
                    }
                    ans = min(ans, max(a, max(b, c)) - min(a, min(b, c)))
                }
            }
        }
        return ans
    }
}
