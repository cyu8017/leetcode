// LeetCode 1717 - Maximum Score From Removing Substrings
// https://leetcode.com/problems/maximum-score-from-removing-substrings/

impl Solution {
    pub fn maximum_gain(s: String, x: i32, y: i32) -> i32 {
        fn remove(text: &[u8], open: u8, close: u8, score: i32) -> (Vec<u8>, i32) {
            let mut stack: Vec<u8> = Vec::with_capacity(text.len());
            let mut gained = 0;
            for &ch in text {
                if !stack.is_empty() && *stack.last().unwrap() == open && ch == close {
                    stack.pop();
                    gained += score;
                } else {
                    stack.push(ch);
                }
            }
            (stack, gained)
        }

        let bytes = s.as_bytes();
        if x >= y {
            let (rest, first) = remove(bytes, b'a', b'b', x);
            let (_, second) = remove(&rest, b'b', b'a', y);
            first + second
        } else {
            let (rest, first) = remove(bytes, b'b', b'a', y);
            let (_, second) = remove(&rest, b'a', b'b', x);
            first + second
        }
    }
}
