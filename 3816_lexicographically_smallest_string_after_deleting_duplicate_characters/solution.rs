// LeetCode 3816 - Lexicographically Smallest String After Deleting Duplicate Characters
// https://leetcode.com/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/

impl Solution {
    pub fn lex_smallest_after_deletion(s: String) -> String {
        let mut cnt = [0i32; 26];
        for c in s.bytes() {
            cnt[(c - b'a') as usize] += 1;
        }
        let mut stk = String::new();
        for c in s.bytes() {
            while !stk.is_empty() {
                let back = stk.as_bytes()[stk.len() - 1];
                if back > c && cnt[(back - b'a') as usize] > 1 {
                    cnt[(back - b'a') as usize] -= 1;
                    stk.pop();
                } else {
                    break;
                }
            }
            stk.push(c as char);
        }
        while !stk.is_empty() {
            let back = stk.as_bytes()[stk.len() - 1];
            if cnt[(back - b'a') as usize] > 1 {
                cnt[(back - b'a') as usize] -= 1;
                stk.pop();
            } else {
                break;
            }
        }
        stk
    }
}
