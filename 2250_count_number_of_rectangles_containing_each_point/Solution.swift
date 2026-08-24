// LeetCode 2250 - Count Number of Rectangles Containing Each Point
// https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

class Solution {
    func countRectangles(_ rectangles: [[Int]], _ points: [[Int]]) -> [Int] {
        var byH = [[Int]](repeating: [], count: 101)
        for r in rectangles { byH[r[1]].append(r[0]) }
        for h in 1...100 { byH[h].sort() }
        return points.map { p in
            let x = p[0], y = p[1]
            var cnt = 0
            for h in y...100 {
                let xs = byH[h]
                var lo = 0, hi = xs.count
                while lo < hi {
                    let mid = (lo + hi) / 2
                    if xs[mid] < x { lo = mid + 1 } else { hi = mid }
                }
                cnt += xs.count - lo
            }
            return cnt
        }
    }
}
