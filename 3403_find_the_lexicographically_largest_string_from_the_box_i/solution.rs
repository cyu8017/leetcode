// LeetCode 3403 - Find the Lexicographically Largest String From the Box I
// https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/

impl Solution {
    pub fn answer_string(word: String, num_friends: i32) -> String {
        if num_friends == 1 {
            return word;
        }
        let n = word.len();
        let max_len = n - (num_friends as usize - 1);
        let mut ans = String::new();
        for i in 0..n {
            let end = (i + max_len).min(n);
            let cand = &word[i..end];
            if cand > ans.as_str() {
                ans = cand.to_string();
            }
        }
        ans
    }
}
