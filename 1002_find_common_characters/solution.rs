// LeetCode 1002 - Find Common Characters
// https://leetcode.com/problems/find-common-characters/

impl Solution {
    pub fn common_chars(words: Vec<String>) -> Vec<String> {
        let mut common = [i32::MAX; 26];
        for w in &words {
            let mut cnt = [0; 26];
            for b in w.bytes() {
                cnt[(b - b'a') as usize] += 1;
            }
            for i in 0..26 {
                common[i] = common[i].min(cnt[i]);
            }
        }
        let mut ans = Vec::new();
        for i in 0..26 {
            for _ in 0..common[i] {
                ans.push(((b'a' + i as u8) as char).to_string());
            }
        }
        ans
    }
}
