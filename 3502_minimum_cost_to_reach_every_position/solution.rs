// LeetCode 3502 - Minimum Cost to Reach Every Position
// https://leetcode.com/problems/minimum-cost-to-reach-every-position/

impl Solution {
    pub fn min_costs(cost: Vec<i32>) -> Vec<i32> {
        let n = cost.len();
        let mut ans = vec![0; n];
        let mut mi = cost[0];
        for i in 0..n {
            mi = mi.min(cost[i]);
            ans[i] = mi;
        }
        ans
    }
}
