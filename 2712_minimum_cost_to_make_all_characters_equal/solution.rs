// LeetCode 2712 - Minimum Cost to Make All Characters Equal
// https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/

impl Solution {
    pub fn minimum_cost(s: String) -> i64 {
        let n = s.len();
        let b = s.as_bytes();
        let mut ans = 0i64;
        for i in 1..n {
            if b[i] != b[i - 1] {
                ans += (i as i64).min((n - i) as i64);
            }
        }
        ans
    }
}
