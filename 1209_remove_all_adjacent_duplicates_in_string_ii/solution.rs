// LeetCode 1209 - Remove All Adjacent Duplicates in String II
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

impl Solution {
    pub fn remove_duplicates(s: String, k: i32) -> String {
        let mut stack: Vec<(u8, i32)> = Vec::new();
        for ch in s.bytes() {
            if let Some(last) = stack.last_mut() {
                if last.0 == ch {
                    last.1 += 1;
                } else {
                    stack.push((ch, 1));
                }
            } else {
                stack.push((ch, 1));
            }
            if stack.last().unwrap().1 == k {
                stack.pop();
            }
        }
        let mut out = Vec::new();
        for (ch, cnt) in stack {
            for _ in 0..cnt {
                out.push(ch);
            }
        }
        String::from_utf8(out).unwrap()
    }
}
