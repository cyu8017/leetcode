struct Solution;

// LeetCode 2555 - Maximize Win From Two Segments
// https://leetcode.com/problems/maximize-win-from-two-segments/

impl Solution {
    pub fn maximize_win(prize_positions: Vec<i32>, k: i32) -> i32 {
        let n = prize_positions.len();
        let mut dp = vec![0; n + 1];
        let mut ans = 0;
        let mut left = 0;
        for right in 0..n {
            while prize_positions[right] - prize_positions[left] > k {
                left += 1;
            }
            let cur = (right - left + 1) as i32;
            if dp[left] + cur > ans {
                ans = dp[left] + cur;
            }
            let mut best = cur;
            if dp[right] > best {
                best = dp[right];
            }
            dp[right + 1] = best;
        }
        ans
    }
}

fn main() {}
