// LeetCode 1812 - Determine Color of a Chessboard Square
// https://leetcode.com/problems/determine-color-of-a-chessboard-square/

impl Solution {
    pub fn square_is_white(coordinates: String) -> bool {
        let bytes = coordinates.as_bytes();
        let col = (bytes[0] - b'a' + 1) as i32;
        let row = (bytes[1] - b'0') as i32;
        (col + row) % 2 == 1
    }
}
