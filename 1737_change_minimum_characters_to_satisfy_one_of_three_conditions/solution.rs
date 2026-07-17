// LeetCode 1737 - Change Minimum Characters to Satisfy One of Three Conditions
// https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/

impl Solution {
    pub fn min_characters(a: String, b: String) -> i32 {
        let mut ca = [0i32; 26];
        let mut cb = [0i32; 26];
        for &byte in a.as_bytes() {
            ca[(byte - b'a') as usize] += 1;
        }
        for &byte in b.as_bytes() {
            cb[(byte - b'a') as usize] += 1;
        }
        let n = a.len() as i32;
        let m = b.len() as i32;
        let max_count = ca.iter().chain(cb.iter()).copied().max().unwrap();
        let mut ans = n + m - max_count;
        let mut pre_a = 0;
        let mut pre_b = 0;
        for code in 0..25 {
            pre_a += ca[code];
            pre_b += cb[code];
            ans = ans.min(n - pre_a + pre_b).min(m - pre_b + pre_a);
        }
        ans
    }
}
