// LeetCode 3042 - Count Prefix and Suffix Pairs I
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

impl Solution {
    pub fn count_prefix_suffix_pairs(words: Vec<String>) -> i32 {
        let mut ans = 0;
        for i in 0..words.len() {
            let s = words[i].as_bytes();
            for j in (i + 1)..words.len() {
                let t = words[j].as_bytes();
                if t.len() >= s.len() && t.starts_with(s) && t.ends_with(s) {
                    ans += 1;
                }
            }
        }
        ans
    }
}
