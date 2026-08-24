// LeetCode 3288 - Length of the Longest Increasing Path
// https://leetcode.com/problems/length-of-the-longest-increasing-path/

class Solution {
    func maxPathLength(_ coordinates: [[Int]], _ k: Int) -> Int {
        let n = coordinates.count
        var arr = [[Int]]()
        for i in 0..<n {
            arr.append([coordinates[i][0], coordinates[i][1], i])
        }
        arr.sort { a, b in
            if a[0] == b[0] { return a[1] > b[1] }
            return a[0] < b[0]
        }
        let kx = coordinates[k][0], ky = coordinates[k][1]
        var left = [Int](), right = [Int]()
        for p in arr {
            if p[0] < kx && p[1] < ky { left.append(p[1]) }
            if p[0] > kx && p[1] > ky { right.append(p[1]) }
        }
        return lis(left) + 1 + lis(right)
    }

    private func lis(_ a: [Int]) -> Int {
        var tails = [Int]()
        for x in a {
            var lo = 0, hi = tails.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if tails[mid] < x { lo = mid + 1 }
                else { hi = mid }
            }
            if lo == tails.count { tails.append(x) }
            else { tails[lo] = x }
        }
        return tails.count
    }
}
