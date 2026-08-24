struct Solution;
// LeetCode 2516 - Take K of Each Character From Left and Right
// https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

impl Solution {
    pub fn take_characters(s: String, k: i32) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let mut cnt = [0i32; 3];
        for &c in b {
            cnt[(c - b'a') as usize] += 1;
        }
        if cnt[0] < k || cnt[1] < k || cnt[2] < k {
            return -1;
        }
        let need = [cnt[0] - k, cnt[1] - k, cnt[2] - k];
        let mut window = [0i32; 3];
        let mut left = 0;
        let mut max_mid = 0;
        for right in 0..n {
            window[(b[right] - b'a') as usize] += 1;
            while window[0] > need[0] || window[1] > need[1] || window[2] > need[2] {
                window[(b[left] - b'a') as usize] -= 1;
                left += 1;
            }
            if right - left + 1 > max_mid {
                max_mid = right - left + 1;
            }
        }
        (n - max_mid) as i32
    }
}

fn main() {}
