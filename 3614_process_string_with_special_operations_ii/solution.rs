// LeetCode 3614 - Process String with Special Operations II
// https://leetcode.com/problems/process-string-with-special-operations-ii/

impl Solution {
    pub fn process_str(s: String, k: i64) -> char {
        let s: Vec<char> = s.chars().collect();
        let mut m: i64 = 0;
        for &c in &s {
            if c == '*' {
                m = if m > 0 { m - 1 } else { 0 };
            } else if c == '#' {
                m <<= 1;
            } else if c != '%' {
                m += 1;
            }
        }
        if k >= m {
            return '.';
        }
        let mut k = k;
        let mut i = s.len() as i32 - 1;
        loop {
            let c = s[i as usize];
            if c == '*' {
                m += 1;
            } else if c == '#' {
                m /= 2;
                if k >= m {
                    k -= m;
                }
            } else if c == '%' {
                k = m - 1 - k;
            } else {
                m -= 1;
                if k == m {
                    return c;
                }
            }
            i -= 1;
        }
    }
}
