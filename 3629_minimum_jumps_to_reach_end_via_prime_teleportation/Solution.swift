// LeetCode 3629 - Minimum Jumps to Reach End via Prime Teleportation
// https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

class Solution {
    func minJumps(_ nums: [Int]) -> Int {
        var mx = 0
        for v in nums { mx = max(mx, v) }
        var factors = Array(repeating: [Int](), count: mx + 1)
        if mx >= 2 {
            for i in 2...mx {
                if factors[i].isEmpty {
                    var j = i
                    while j <= mx { factors[j].append(i); j += i }
                }
            }
        }
        let n = nums.count
        var g = [Int: [Int]]()
        for i in 0..<n {
            for p in factors[nums[i]] { g[p, default: []].append(i) }
        }
        var ans = 0
        var vis = Array(repeating: false, count: n)
        vis[0] = true
        var q = [0]
        while true {
            var nq = [Int]()
            for i in q {
                if i == n - 1 { return ans }
                var idx = g[nums[i]] ?? []
                idx.append(i + 1)
                if i > 0 { idx.append(i - 1) }
                for j in idx {
                    if j >= 0 && j < n && !vis[j] {
                        vis[j] = true
                        nq.append(j)
                    }
                }
                g[nums[i]] = []
            }
            q = nq
            ans += 1
        }
    }
}
