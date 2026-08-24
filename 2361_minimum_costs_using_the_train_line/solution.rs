// LeetCode 2361 - Minimum Costs Using the Train Line
// https://leetcode.com/problems/minimum-costs-using-the-train-line/

impl Solution {
    pub fn minimum_costs(regular: Vec<i32>, express: Vec<i32>, express_cost: i32) -> Vec<i64> {
        let n = regular.len();
        let mut ans = vec![0i64; n];
        let mut reg = 0i64;
        let mut exp = express_cost as i64;
        for i in 0..n {
            let next_reg = (reg + regular[i] as i64).min(exp + express[i] as i64);
            let next_exp = (reg + regular[i] as i64 + express_cost as i64).min(exp + express[i] as i64);
            reg = next_reg;
            exp = next_exp;
            ans[i] = reg.min(exp);
        }
        ans
    }
}
