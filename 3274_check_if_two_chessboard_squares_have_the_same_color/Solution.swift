// LeetCode 3274 - Check if Two Chessboard Squares Have the Same Color
// https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/

class Solution {
    func checkTwoChessboards(_ coordinate1: String, _ coordinate2: String) -> Bool {
        let a = Array(coordinate1), b = Array(coordinate2)
        let c1 = Int(a[0].asciiValue! - Character("a").asciiValue!) + Int(a[1].asciiValue! - Character("1").asciiValue!)
        let c2 = Int(b[0].asciiValue! - Character("a").asciiValue!) + Int(b[1].asciiValue! - Character("1").asciiValue!)
        return c1 % 2 == c2 % 2
    }
}
