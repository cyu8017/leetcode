struct Solution;
// LeetCode 2931 - Maximum Spending After Buying Items
// https://leetcode.com/problems/maximum-spending-after-buying-items/

impl Solution {
    pub fn max_spending(values: Vec<Vec<i32>>) -> i64 {
        let m = values.len();
        let n = values[0].len();
        let mut idx = vec![n as i32 - 1; m];
        let mut ans = 0i64;
        let mut day = 1i64;
        let total = m * n;
        for _ in 0..total {
            let mut best_i = 0usize;
            let mut best_v = 1i64 << 60;
            for i in 0..m {
                if idx[i] >= 0 && (values[i][idx[i] as usize] as i64) < best_v {
                    best_v = values[i][idx[i] as usize] as i64;
                    best_i = i;
                }
            }
            ans += best_v * day;
            idx[best_i] -= 1;
            day += 1;
        }
        ans
    }
}

fn main() {}
