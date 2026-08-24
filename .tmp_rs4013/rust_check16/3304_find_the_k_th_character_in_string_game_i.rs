struct Solution;
// LeetCode 3304 - Find the K-th Character in String Game I
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

impl Solution {
    pub fn kth_character(k: i32) -> char {
        let mut s = vec![b'a'];
        while s.len() < k as usize {
            let n = s.len();
            for i in 0..n {
                s.push(b'a' + (s[i] - b'a' + 1) % 26);
            }
        }
        s[(k - 1) as usize] as char
    }
}

fn main() {}
