// LeetCode 1499 - Max Value of Equation
// https://leetcode.com/problems/max-value-of-equation/

class Solution {
    func findMaxValueOfEquation(_ points: [[Int]], _ k: Int) -> Int {
        var q = [(Int, Int)]() // (x, y-x)
        var ans = Int.min / 4
        for p in points {
            let x = p[0], y = p[1]
            while !q.isEmpty && x - q[0].0 > k { q.removeFirst() }
            if !q.isEmpty { ans = max(ans, x + y + q[0].1) }
            let value = y - x
            while !q.isEmpty && q.last!.1 <= value { q.removeLast() }
            q.append((x, value))
        }
        return ans
    }
}
