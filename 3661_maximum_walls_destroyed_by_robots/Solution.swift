// LeetCode 3661 - Maximum Walls Destroyed by Robots
// https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

class Solution {
    var arr = [[Int]]()
    var walls = [Int]()
    var memo = [Int: Int]()

    func lowerBound(_ a: [Int], _ target: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] < target { lo = mid + 1 } else { hi = mid }
        }
        return lo
    }

    func dfs(_ i: Int, _ j: Int) -> Int {
        if i < 0 { return 0 }
        let key = (i << 1) | j
        if let v = memo[key] { return v }
        var left = arr[i][0] - arr[i][1]
        if i > 0 { left = max(left, arr[i - 1][0] + 1) }
        var l = lowerBound(walls, left)
        var r = lowerBound(walls, arr[i][0] + 1)
        var ans = dfs(i - 1, 0) + (r - l)
        var right = arr[i][0] + arr[i][1]
        if i + 1 < arr.count {
            if j == 0 { right = min(right, arr[i + 1][0] - arr[i + 1][1] - 1) }
            else { right = min(right, arr[i + 1][0] - 1) }
        }
        l = lowerBound(walls, arr[i][0])
        r = lowerBound(walls, right + 1)
        ans = max(ans, dfs(i - 1, 1) + (r - l))
        memo[key] = ans
        return ans
    }

    func maxWalls(_ robots: [Int], _ distance: [Int], _ walls: [Int]) -> Int {
        let n = robots.count
        arr = (0..<n).map { [robots[$0], distance[$0]] }
        arr.sort { $0[0] < $1[0] }
        self.walls = walls.sorted()
        memo = [:]
        return dfs(n - 1, 1)
    }
}
