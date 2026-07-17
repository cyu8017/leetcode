// LeetCode 1782 - Count Pairs Of Nodes
// https://leetcode.com/problems/count-pairs-of-nodes/

class Solution {
    func countPairs(_ n: Int, _ edges: [[Int]], _ queries: [Int]) -> [Int] {
        var deg = [Int](repeating: 0, count: n + 1)
        var shared = [Int: Int]()
        for edge in edges {
            let a = min(edge[0], edge[1])
            let b = max(edge[0], edge[1])
            deg[a] += 1
            deg[b] += 1
            shared[a * 100000 + b, default: 0] += 1
        }
        let sortedDeg = Array(deg[1...]).sorted()
        var ans = [Int]()
        ans.reserveCapacity(queries.count)
        for q in queries {
            var res = 0
            var left = 0
            var right = n - 1
            while left < right {
                if sortedDeg[left] + sortedDeg[right] > q {
                    res += right - left
                    right -= 1
                } else {
                    left += 1
                }
            }
            for (key, count) in shared {
                let a = key / 100000
                let b = key % 100000
                let sum = deg[a] + deg[b]
                if sum > q && q >= sum - count {
                    res -= 1
                }
            }
            ans.append(res)
        }
        return ans
    }
}
