// LeetCode 2843 - Count Symmetric Integers
// https://leetcode.com/problems/count-symmetric-integers/

impl Solution {
    pub fn count_symmetric_integers(low: i32, high: i32) -> i32 {
        let mut ans = 0;
        for x in low..=high {
            let s = x.to_string();
            let b = s.as_bytes();
            if b.len() % 2 == 1 {
                continue;
            }
            let mid = b.len() / 2;
            let mut a = 0;
            let mut c = 0;
            for i in 0..mid {
                a += (b[i] - b'0') as i32;
                c += (b[mid + i] - b'0') as i32;
            }
            if a == c {
                ans += 1;
            }
        }
        ans
    }
}
