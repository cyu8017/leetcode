// LeetCode 3588 - Find Maximum Area of a Triangle
// https://leetcode.com/problems/find-maximum-area-of-a-triangle/

class Solution {
    func maxArea(_ coords: [[Int]]) -> Int {
        var coords = coords
        var ans = calc(coords)
        for i in 0..<coords.count {
            let t = coords[i][0]
            coords[i][0] = coords[i][1]
            coords[i][1] = t
        }
        ans = max(ans, calc(coords))
        return ans > 0 ? ans : -1
    }

    func calc(_ coords: [[Int]]) -> Int {
        var mn = 1_000_000_000, mx = 0
        var f = [Int: Int]()
        var g = [Int: Int]()
        for c in coords {
            let x = c[0], y = c[1]
            mn = min(mn, x)
            mx = max(mx, x)
            if f[x] != nil {
                f[x] = min(f[x]!, y)
                g[x] = max(g[x]!, y)
            } else {
                f[x] = y
                g[x] = y
            }
        }
        var ans = 0
        for (x, y) in f {
            let d = g[x]! - y
            ans = max(ans, d * max(mx - x, x - mn))
        }
        return ans
    }
}
