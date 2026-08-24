// LeetCode 2087 - Minimum Cost Homecoming of a Robot in a Grid
// https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/

impl Solution {
    pub fn min_cost(
        start_pos: Vec<i32>,
        home_pos: Vec<i32>,
        row_costs: Vec<i32>,
        col_costs: Vec<i32>,
    ) -> i32 {
        let mut ans = 0;
        let (sr, sc, hr, hc) = (start_pos[0], start_pos[1], home_pos[0], home_pos[1]);
        if sr < hr {
            for r in sr + 1..=hr {
                ans += row_costs[r as usize];
            }
        } else {
            for r in (hr..sr).rev() {
                ans += row_costs[r as usize];
            }
        }
        if sc < hc {
            for c in sc + 1..=hc {
                ans += col_costs[c as usize];
            }
        } else {
            for c in (hc..sc).rev() {
                ans += col_costs[c as usize];
            }
        }
        ans
    }
}
