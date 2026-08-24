// LeetCode 2836 - Maximize Value of Function in a Ball Passing Game
// https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/

impl Solution {
    pub fn get_max_function_value(receiver: Vec<i32>, k: i64) -> i64 {
        let n = receiver.len();
        const LOG: usize = 36;
        let mut up = vec![vec![0usize; n]; LOG];
        let mut sum = vec![vec![0i64; n]; LOG];
        for i in 0..n {
            up[0][i] = receiver[i] as usize;
            sum[0][i] = receiver[i] as i64;
        }
        for j in 1..LOG {
            for i in 0..n {
                let mid = up[j - 1][i];
                up[j][i] = up[j - 1][mid];
                sum[j][i] = sum[j - 1][i] + sum[j - 1][mid];
            }
        }
        let mut ans = 0i64;
        for i in 0..n {
            let mut cur = i;
            let mut total = i as i64;
            let mut kk = k;
            for j in 0..LOG {
                if (kk & (1i64 << j)) != 0 {
                    total += sum[j][cur];
                    cur = up[j][cur];
                }
            }
            ans = ans.max(total);
        }
        ans
    }
}
