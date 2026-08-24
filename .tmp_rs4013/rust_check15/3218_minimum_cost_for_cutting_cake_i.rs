struct Solution;
// LeetCode 3218 - Minimum Cost for Cutting Cake I
// https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/

impl Solution {
    pub fn minimum_cost(m: i32, n: i32, mut horizontal_cut: Vec<i32>, mut vertical_cut: Vec<i32>) -> i32 {
        horizontal_cut.sort_unstable_by(|a, b| b.cmp(a));
        vertical_cut.sort_unstable_by(|a, b| b.cmp(a));
        let mut i = 0;
        let mut j = 0;
        let mut h = 1;
        let mut v = 1;
        let mut ans = 0;
        while i < m - 1 || j < n - 1 {
            if j == n - 1 || (i < m - 1 && horizontal_cut[i as usize] > vertical_cut[j as usize]) {
                ans += horizontal_cut[i as usize] * v;
                h += 1;
                i += 1;
            } else {
                ans += vertical_cut[j as usize] * h;
                v += 1;
                j += 1;
            }
        }
        ans
    }
}

fn main() {}
