// LeetCode 3454 - Separate Squares II
// https://leetcode.com/problems/separate-squares-ii/

class Solution {
    func separateSquares(_ squares: [[Int]]) -> Double {
        var total = 0.0
        for sq in squares {
            let l = Double(sq[2])
            total += l * l
        }
        var lo = 0.0, hi = 2e9
        for _ in 0..<60 {
            let mid = (lo + hi) / 2
            if areaBelow(squares, mid) * 2 < total { lo = mid }
            else { hi = mid }
        }
        return hi
    }

    private func areaBelow(_ squares: [[Int]], _ y: Double) -> Double {
        var below = 0.0
        for sq in squares {
            let yi = Double(sq[1]), l = Double(sq[2])
            let top = yi + l
            if y <= yi { continue }
            else if y >= top { below += l * l }
            else { below += l * (y - yi) }
        }
        return below
    }
}
