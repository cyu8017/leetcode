// LeetCode 1415 - The k-th Lexicographical String of All Happy Strings of Length n
// https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

impl Solution {
    pub fn get_happy_string(n: i32, k: i32) -> String {
        let mut answer = Vec::new();
        fn build(path: String, n: usize, answer: &mut Vec<String>) {
            if path.len() == n {
                answer.push(path);
                return;
            }
            for ch in ['a', 'b', 'c'] {
                if path.chars().last() != Some(ch) {
                    let mut next = path.clone();
                    next.push(ch);
                    build(next, n, answer);
                }
            }
        }
        build(String::new(), n as usize, &mut answer);
        if (k as usize) <= answer.len() {
            answer[(k - 1) as usize].clone()
        } else {
            String::new()
        }
    }
}
