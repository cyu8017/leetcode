struct Solution;
// LeetCode 3258 - Count Substrings That Satisfy K-Constraint I
// https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/

impl Solution {
    pub fn count_k_constraint_substrings(s: String, k: i32) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let mut ans = 0;
        for i in 0..n {
            let mut z = 0;
            let mut o = 0;
            for j in i..n {
                if b[j] == b'0' {
                    z += 1;
                } else {
                    o += 1;
                }
                if z <= k || o <= k {
                    ans += 1;
                } else {
                    break;
                }
            }
        }
        ans
    }
}

fn main() {}
