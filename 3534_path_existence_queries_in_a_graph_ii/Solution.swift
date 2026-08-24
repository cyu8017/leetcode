// LeetCode 3534 - Path Existence Queries in a Graph II
// https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/

class Solution {
    func pathExistenceQueries(_ n: Int, _ nums: [Int], _ maxDiff: Int, _ queries: [[Int]]) -> [Int] {
        var pairs = (0..<n).map { [nums[$0], $0] }
        pairs.sort { $0[0] < $1[0] }
        let m = 20
        var f = Array(repeating: Array(repeating: 0, count: m), count: n)
        var r = n - 1
        for l in stride(from: n - 1, through: 0, by: -1) {
            while pairs[r][0] - pairs[l][0] > maxDiff { r -= 1 }
            let i = pairs[l][1], j = pairs[r][1]
            f[i][0] = j
            for k in 1..<m { f[i][k] = f[f[i][k - 1]][k - 1] }
        }
        var ans = [Int]()
        for q in queries {
            var i = q[0], j = q[1]
            if nums[i] > nums[j] { swap(&i, &j) }
            if i == j { ans.append(0); continue }
            if nums[i] == nums[j] { ans.append(1); continue }
            var d = 0
            for k in stride(from: m - 1, through: 0, by: -1) {
                if nums[f[i][k]] < nums[j] {
                    d |= 1 << k
                    i = f[i][k]
                }
            }
            if nums[f[i][0]] < nums[j] { ans.append(-1) }
            else { ans.append(d + 1) }
        }
        return ans
    }
}
