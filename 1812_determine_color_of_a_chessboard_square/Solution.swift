// LeetCode 1812 - Determine Color of a Chessboard Square
// https://leetcode.com/problems/determine-color-of-a-chessboard-square/

class Solution {
    func squareIsWhite(_ coordinates: String) -> Bool {
        let chars = Array(coordinates)
        let col = Int(chars[0].asciiValue! - Character("a").asciiValue!) + 1
        let row = Int(String(chars[1]))!
        return (col + row) % 2 == 1
    }
}
