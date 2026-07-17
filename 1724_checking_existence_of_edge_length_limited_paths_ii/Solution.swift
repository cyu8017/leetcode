// LeetCode 1724 - Checking Existence of Edge Length Limited Paths II
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths-ii/

class DistanceLimitedPathsExist {
    private var weights = [Int]()
    private var versions = [[Int]]()

    init(_ n: Int, _ edgeList: [[Int]]) {
        let edges = edgeList
            .map { [$0[2], $0[0], $0[1]] }
            .sorted { a, b in
                if a[0] != b[0] { return a[0] < b[0] }
                if a[1] != b[1] { return a[1] < b[1] }
                return a[2] < b[2]
            }
        var parent = Array(0..<n)
        var size = [Int](repeating: 1, count: n)
        func find(_ start: Int) -> Int {
            var x = start
            while parent[x] != x {
                parent[x] = parent[parent[x]]
                x = parent[x]
            }
            return x
        }
        var i = 0
        while i < edges.count {
            let weight = edges[i][0]
            while i < edges.count && edges[i][0] == weight {
                var ra = find(edges[i][1])
                var rb = find(edges[i][2])
                if ra != rb {
                    if size[ra] < size[rb] {
                        swap(&ra, &rb)
                    }
                    parent[rb] = ra
                    size[ra] += size[rb]
                }
                i += 1
            }
            weights.append(weight)
            versions.append(parent)
        }
    }

    func query(_ p: Int, _ q: Int, _ limit: Int) -> Bool {
        var lo = 0
        var hi = weights.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if weights[mid] < limit {
                lo = mid + 1
            } else {
                hi = mid
            }
        }
        let idx = lo - 1
        if idx < 0 { return p == q }
        let parent = versions[idx]
        func find(_ start: Int) -> Int {
            var x = start
            while parent[x] != x {
                x = parent[x]
            }
            return x
        }
        return find(p) == find(q)
    }
}
