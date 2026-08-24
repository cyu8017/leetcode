// LeetCode 2417 - Closest Fair Integer
// https://leetcode.com/problems/closest-fair-integer/

impl Solution {
    pub fn closest_fair(n: i32) -> i32 {
        let mut x = n;
        loop {
            let s = x.to_string();
            if s.len() % 2 != 0 {
                let mut p = 1i32;
                for _ in 0..s.len() {
                    p *= 10;
                }
                return Self::closest_fair(p);
            }
            let mut even = 0;
            let mut odd = 0;
            for c in s.bytes() {
                if (c - b'0') % 2 == 0 {
                    even += 1;
                } else {
                    odd += 1;
                }
            }
            if even == odd {
                return x;
            }
            x += 1;
        }
    }
}
