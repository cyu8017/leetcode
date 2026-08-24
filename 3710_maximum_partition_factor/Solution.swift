// LeetCode 3710 - Maximum Partition Factor
// https://leetcode.com/problems/maximum-partition-factor/

class Solution {
    var points = [[Int]]()
    var n = 0

    func dist(_ i: Int, _ j: Int) -> Int {
        abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
    }

    func ok(_ d: Int) -> Bool {
        var g = Array(repeating: [Int](), count: n)
        for i in 0..<n {
            if i + 1 < n {
                for j in (i + 1)..<n {
                    if dist(i, j) < d {
                        g[i].append(j)
                        g[j].append(i)
                    }
                }
            }
        }
        var color = Array(repeating: -1, count: n)
        for i in 0..<n {
            if color[i] != -1 { continue }
            var q = [i]
            color[i] = 0
            var head = 0
            while head < q.count {
                let u = q[head]; head += 1
                for v in g[u] {
                    if color[v] == -1 {
                        color[v] = color[u] ^ 1
                        q.append(v)
                    } else if color[v] == color[u] { return false }
                }
            }
        }
        return true
    }

    func maxPartitionFactor(_ points: [[Int]]) -> Int {
        self.points = points
        n = points.count
        if n == 2 { return 0 }
        var lo = 0, hi = 0
        for i in 0..<n {
            if i + 1 < n {
                for j in (i + 1)..<n { hi = max(hi, dist(i, j)) }
            }
        }
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            if ok(mid) { lo = mid } else { hi = mid - 1 }
        }
        return lo
    }
}
