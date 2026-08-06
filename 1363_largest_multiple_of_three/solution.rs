// LeetCode 1363 - Largest Multiple of Three
// https://leetcode.com/problems/largest-multiple-of-three/

impl Solution {
    pub fn largest_multiple_of_three(digits: Vec<i32>) -> String {
        let mut cnt = [0; 10];
        let mut rem = 0;
        for &d in &digits {
            cnt[d as usize] += 1;
            rem += d;
        }
        rem %= 3;
        let mut remove = |r: i32, mut k: i32| -> bool {
            let mut d = r;
            while d < 10 {
                while cnt[d as usize] > 0 && k > 0 {
                    cnt[d as usize] -= 1;
                    k -= 1;
                }
                if k == 0 {
                    return true;
                }
                d += 3;
            }
            false
        };
        if rem != 0 && !remove(rem, 1) {
            remove(3 - rem, 2);
        }
        let mut s = String::new();
        for d in (0..=9).rev() {
            for _ in 0..cnt[d] {
                s.push((b'0' + d as u8) as char);
            }
        }
        if !s.is_empty() && s.starts_with('0') {
            "0".to_string()
        } else {
            s
        }
    }
}
