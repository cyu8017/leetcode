// LeetCode 2081 - Sum of k-Mirror Numbers
// https://leetcode.com/problems/sum-of-k-mirror-numbers/

impl Solution {
    fn is_pal_base(mut x: i64, base: i32) -> bool {
        let mut digits = Vec::new();
        while x > 0 {
            digits.push(x % base as i64);
            x /= base as i64;
        }
        let mut l = 0;
        let mut r = digits.len() as i32 - 1;
        while l < r {
            if digits[l as usize] != digits[r as usize] {
                return false;
            }
            l += 1;
            r -= 1;
        }
        true
    }

    pub fn k_mirror(k: i32, n: i32) -> i64 {
        let mut ans = 0i64;
        let mut count = 0;
        let mut length = 1;
        while count < n {
            let mut start = 1;
            for _ in 1..(length + 1) / 2 {
                start *= 10;
            }
            let end = start * 10;
            let mut half = start;
            while half < end && count < n {
                let mut pal = half as i64;
                if length % 2 == 0 {
                    let mut x = half;
                    while x > 0 {
                        pal = pal * 10 + (x % 10) as i64;
                        x /= 10;
                    }
                } else {
                    let mut x = half / 10;
                    while x > 0 {
                        pal = pal * 10 + (x % 10) as i64;
                        x /= 10;
                    }
                }
                if Self::is_pal_base(pal, k) {
                    ans += pal;
                    count += 1;
                }
                half += 1;
            }
            length += 1;
        }
        ans
    }
}
