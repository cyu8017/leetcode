// LeetCode 3001 - Minimum Moves to Capture The Queen
// https://leetcode.com/problems/minimum-moves-to-capture-the-queen/

class Solution {
    func minMovesToCaptureTheQueen(_ a: Int, _ b: Int, _ c: Int, _ d: Int, _ e: Int, _ f: Int) -> Int {
        if a == e && (c != a || (d - b) * (d - f) > 0) { return 1 }
        if b == f && (d != b || (c - a) * (c - e) > 0) { return 1 }
        if c - e == d - f && (a - e != b - f || (a - c) * (a - e) > 0) { return 1 }
        if c - e == f - d && (a - e != f - b || (a - c) * (a - e) > 0) { return 1 }
        return 2
    }
}
