// LeetCode 2511 - Maximum Enemy Forts That Can Be Captured
// https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

impl Solution {
    pub fn capture_forts(forts: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut prev = -1i32;
        for i in 0..forts.len() {
            if forts[i] != 0 {
                if prev >= 0 && forts[prev as usize] == -forts[i] {
                    let d = i as i32 - prev - 1;
                    if d > ans {
                        ans = d;
                    }
                }
                prev = i as i32;
            }
        }
        ans
    }
}
