// LeetCode 2904 - Shortest and Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

impl Solution {
    pub fn shortest_beautiful_substring(s: String, k: i32) -> String {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut ans = String::new();
        for i in 0..n {
            let mut ones = 0;
            for j in i..n {
                if bytes[j] == b'1' {
                    ones += 1;
                }
                if ones == k {
                    let cand = s[i..=j].to_string();
                    if ans.is_empty()
                        || cand.len() < ans.len()
                        || (cand.len() == ans.len() && cand < ans)
                    {
                        ans = cand;
                    }
                    break;
                }
                if ones > k {
                    break;
                }
            }
        }
        ans
    }
}
