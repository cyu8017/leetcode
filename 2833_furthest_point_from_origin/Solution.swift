// LeetCode 2833 - Furthest Point From Origin
// https://leetcode.com/problems/furthest-point-from-origin/

class Solution {
    func furthestDistanceFromOrigin(_ moves: String) -> Int {
        var left = 0, right = 0, u = 0
        for c in moves {
            if c == "L" { left += 1 }
            else if c == "R" { right += 1 }
            else { u += 1 }
        }
        return abs(left - right) + u
    }
}
