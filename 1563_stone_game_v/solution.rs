// LeetCode 1563 - Stone Game V
// https://leetcode.com/problems/stone-game-v/

impl Solution {
    pub fn stone_game_v(stone_value: Vec<i32>) -> i32 {
        let n = stone_value.len();
        if n == 0 {
            return 0;
        }
        let mut pre = vec![0; n + 1];
        for i in 0..n {
            pre[i + 1] = pre[i] + stone_value[i];
        }
        let mut dp = vec![vec![0; n]; n];
        let mut left = vec![vec![0; n]; n];
        let mut right = vec![vec![0; n]; n];
        for i in 0..n {
            left[i][i] = stone_value[i];
            right[i][i] = stone_value[i];
        }
        for length in 2..=n {
            for i in 0..=n - length {
                let j = i + length - 1;
                let mut lo = i as i32;
                let mut hi = (j - 1) as i32;
                while lo <= hi {
                    let mid = (lo + hi) / 2;
                    if 2 * (pre[mid as usize + 1] - pre[i]) >= pre[j + 1] - pre[i] {
                        hi = mid - 1;
                    } else {
                        lo = mid + 1;
                    }
                }
                let split = lo as usize;
                let left_sum = pre[split + 1] - pre[i];
                let right_sum = pre[j + 1] - pre[split + 1];
                let mut best = right[split + 1][j];
                if left_sum == right_sum {
                    best = best.max(left[i][split]);
                } else if split > i {
                    best = best.max(left[i][split - 1]);
                }
                dp[i][j] = best;
                let total = pre[j + 1] - pre[i];
                left[i][j] = left[i][j - 1].max(total + best);
                right[i][j] = right[i + 1][j].max(total + best);
            }
        }
        dp[0][n - 1]
    }
}
