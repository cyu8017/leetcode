// LeetCode 3817 - Good Indices In A Digit String
// https://leetcode.com/problems/good-indices-in-a-digit-string/

impl Solution {
    pub fn good_indices(s: String) -> Vec<i32> {
        let mut ans = Vec::new();
        for i in 0..s.len() {
            let t = i.to_string();
            let k = t.len();
            if i + 1 >= k && &s[i + 1 - k..i + 1] == t {
                ans.push(i as i32);
            }
        }
        ans
    }
}
