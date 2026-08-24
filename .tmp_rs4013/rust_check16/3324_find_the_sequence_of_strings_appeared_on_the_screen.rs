struct Solution;
// LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen
// https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

impl Solution {
    pub fn string_sequence(target: String) -> Vec<String> {
        let mut ans = Vec::new();
        let mut cur = String::new();
        for ch in target.chars() {
            cur.push('a');
            ans.push(cur.clone());
            while cur.chars().last().unwrap() != ch {
                let mut bytes = cur.into_bytes();
                let last = bytes.len() - 1;
                bytes[last] += 1;
                cur = String::from_utf8(bytes).unwrap();
                ans.push(cur.clone());
            }
        }
        ans
    }
}

fn main() {}
