struct Solution;
// LeetCode 2896 - Apply Operations to Make Two Strings Equal
// https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/

impl Solution {
    pub fn min_operations(s1: String, s2: String, x: i32) -> i32 {
        let a = s1.as_bytes();
        let b = s2.as_bytes();
        let mut diff = Vec::new();
        for i in 0..a.len() {
            if a[i] != b[i] {
                diff.push(i as i32);
            }
        }
        let m = diff.len();
        if m % 2 == 1 {
            return -1;
        }
        if m == 0 {
            return 0;
        }
        let inf = 1 << 30;
        let mut dp2 = vec![inf; m + 1];
        dp2[0] = 0;
        for i in 0..m {
            if dp2[i] >= inf {
                continue;
            }
            if i + 1 < m {
                let mut cand = diff[i + 1] - diff[i];
                if cand > x {
                    cand = x;
                }
                if dp2[i] + cand < dp2[i + 2] {
                    dp2[i + 2] = dp2[i] + cand;
                }
            }
        }
        if dp2[m] >= inf { -1 } else { dp2[m] }
    }
}

fn main() {}
