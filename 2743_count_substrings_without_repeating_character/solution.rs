// LeetCode 2743 - Count Substrings Without Repeating Character
// https://leetcode.com/problems/count-substrings-without-repeating-character/

impl Solution {
    pub fn number_of_special_substrings(s: String) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let mut ans = 0;
        let mut left = 0;
        let mut cnt = [0i32; 26];
        for i in 0..n {
            let c = (b[i] - b'a') as usize;
            cnt[c] += 1;
            while cnt[c] > 1 {
                cnt[(b[left] - b'a') as usize] -= 1;
                left += 1;
            }
            ans += (i - left + 1) as i32;
        }
        ans
    }
}
