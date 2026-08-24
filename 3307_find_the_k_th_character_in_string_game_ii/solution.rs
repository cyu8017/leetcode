// LeetCode 3307 - Find the K-th Character in String Game II
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

impl Solution {
    pub fn kth_character(mut k: i64, operations: Vec<i32>) -> char {
        let mut shift = 0;
        let mut ops = operations;
        while !ops.is_empty() {
            let op = ops.pop().unwrap();
            let half = 1i64 << ops.len();
            if k > half {
                k -= half;
                if op == 1 {
                    shift += 1;
                }
            }
        }
        (b'a' + (shift % 26) as u8) as char
    }
}
