// LeetCode 0038 - Count and Say
// https://leetcode.com/problems/count-and-say/

impl Solution {
    pub fn count_and_say(n: i32) -> String {
        let mut term = String::from("1");

        for _ in 1..n {
            let bytes = term.as_bytes();
            let mut next_term = String::new();
            let mut index = 0usize;

            while index < bytes.len() {
                let mut count = 1usize;
                while index + count < bytes.len() && bytes[index + count] == bytes[index] {
                    count += 1;
                }
                next_term.push_str(&count.to_string());
                next_term.push(bytes[index] as char);
                index += count;
            }

            term = next_term;
        }

        term
    }
}
