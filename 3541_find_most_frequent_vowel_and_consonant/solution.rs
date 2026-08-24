// LeetCode 3541 - Find Most Frequent Vowel and Consonant
// https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

impl Solution {
    pub fn max_freq_sum(s: String) -> i32 {
        let mut cnt = [0i32; 26];
        for c in s.bytes() {
            cnt[(c - b'a') as usize] += 1;
        }
        let mut a = 0;
        let mut b = 0;
        for i in 0..26 {
            let c = (i as u8 + b'a') as char;
            if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' {
                a = a.max(cnt[i]);
            } else {
                b = b.max(cnt[i]);
            }
        }
        a + b
    }
}
