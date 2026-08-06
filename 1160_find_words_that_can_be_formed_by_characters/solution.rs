// LeetCode 1160 - Find Words That Can Be Formed by Characters
// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

impl Solution {
    pub fn count_characters(words: Vec<String>, chars: String) -> i32 {
        let mut have = [0; 26];
        for b in chars.bytes() {
            have[(b - b'a') as usize] += 1;
        }
        let mut ans = 0;
        for w in words {
            let mut need = [0; 26];
            let mut ok = true;
            for b in w.bytes() {
                let i = (b - b'a') as usize;
                need[i] += 1;
                if need[i] > have[i] {
                    ok = false;
                    break;
                }
            }
            if ok {
                ans += w.len() as i32;
            }
        }
        ans
    }
}
