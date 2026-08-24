// LeetCode 3582 - Generate Tag for Video Caption
// https://leetcode.com/problems/generate-tag-for-video-caption/

impl Solution {
    pub fn generate_tag(caption: String) -> String {
        let mut ans = String::from("#");
        let mut i = 0;
        for word in caption.split_whitespace() {
            let mut word: Vec<u8> = word.bytes().map(|c| c.to_ascii_lowercase()).collect();
            if i == 0 {
                ans.push_str(&String::from_utf8(word).unwrap());
            } else {
                if !word.is_empty() {
                    word[0] = word[0].to_ascii_uppercase();
                }
                ans.push_str(&String::from_utf8(word).unwrap());
            }
            if ans.len() >= 100 {
                break;
            }
            i += 1;
        }
        if ans.len() > 100 {
            ans.truncate(100);
        }
        ans
    }
}
