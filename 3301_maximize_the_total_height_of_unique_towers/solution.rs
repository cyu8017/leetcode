// LeetCode 3301 - Maximize the Total Height of Unique Towers
// https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/

impl Solution {
    pub fn maximum_total_sum(mut maximum_height: Vec<i32>) -> i64 {
        maximum_height.sort_unstable_by(|a, b| b.cmp(a));
        let mut ans = 0i64;
        let mut prev = 10i64.pow(18);
        for h in maximum_height {
            let mut cur = h as i64;
            if cur >= prev {
                cur = prev - 1;
            }
            if cur <= 0 {
                return -1;
            }
            ans += cur;
            prev = cur;
        }
        ans
    }
}
