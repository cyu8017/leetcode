struct Solution;
// LeetCode 3445 - Maximum Difference Between Even and Odd Frequency II
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/

impl Solution {
    pub fn max_difference(s: String, k: i32) -> i32 {
        let n = s.len();
        let bytes = s.as_bytes();
        let mut ans = -1_000_000_000;
        for a in 0..5 {
            for b in 0..5 {
                if a == b {
                    continue;
                }
                let mut pref_a = vec![0; n + 1];
                let mut pref_b = vec![0; n + 1];
                for i in 0..n {
                    pref_a[i + 1] = pref_a[i];
                    pref_b[i + 1] = pref_b[i];
                    if (bytes[i] - b'0') as i32 == a {
                        pref_a[i + 1] += 1;
                    }
                    if (bytes[i] - b'0') as i32 == b {
                        pref_b[i + 1] += 1;
                    }
                }
                for i in 0..n {
                    let mut j = i + k as usize - 1;
                    while j < n {
                        let fa = pref_a[j + 1] - pref_a[i];
                        let fb = pref_b[j + 1] - pref_b[i];
                        if fa % 2 == 1 && fb % 2 == 0 && fb > 0 && fa - fb > ans {
                            ans = fa - fb;
                        }
                        j += 1;
                    }
                }
            }
        }
        ans
    }
}

fn main() {}
