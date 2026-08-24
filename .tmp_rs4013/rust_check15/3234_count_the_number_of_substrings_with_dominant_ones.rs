struct Solution;
// LeetCode 3234 - Count the Number of Substrings With Dominant Ones
// https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/

impl Solution {
    pub fn number_of_substrings(s: String) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let mut nxt = vec![0; n + 1];
        nxt[n] = n;
        for i in (0..n).rev() {
            nxt[i] = nxt[i + 1];
            if b[i] == b'0' {
                nxt[i] = i;
            }
        }
        let mut ans = 0;
        for i in 0..n {
            let mut cnt0 = if b[i] == b'0' { 1 } else { 0 };
            let mut j = i;
            while j < n && (cnt0 as i64) * (cnt0 as i64) <= n as i64 {
                let cnt1 = nxt[j + 1] as i32 - i as i32 - cnt0;
                if cnt1 >= cnt0 * cnt0 {
                    ans += (nxt[j + 1] as i32 - j as i32).min(cnt1 - cnt0 * cnt0 + 1);
                }
                j = nxt[j + 1];
                cnt0 += 1;
            }
        }
        ans
    }
}

fn main() {}
