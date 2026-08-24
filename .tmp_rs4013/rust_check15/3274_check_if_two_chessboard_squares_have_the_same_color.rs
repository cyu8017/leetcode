struct Solution;
// LeetCode 3274 - Check if Two Chessboard Squares Have the Same Color
// https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/

impl Solution {
    pub fn check_two_chessboards(coordinate1: String, coordinate2: String) -> bool {
        let b1 = coordinate1.as_bytes();
        let b2 = coordinate2.as_bytes();
        let c1 = (b1[0] - b'a') as i32 + (b1[1] - b'1') as i32;
        let c2 = (b2[0] - b'a') as i32 + (b2[1] - b'1') as i32;
        c1 % 2 == c2 % 2
    }
}

fn main() {}
