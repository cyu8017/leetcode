// LeetCode 1140 - Stone Game II
// https://leetcode.com/problems/stone-game-ii/

impl Solution {
    pub fn stone_game_ii(piles: Vec<i32>) -> i32 {
        let n = piles.len();
        let mut suffix = vec![0; n + 1];
        for i in (0..n).rev() {
            suffix[i] = suffix[i + 1] + piles[i];
        }
        let mut memo = vec![vec![-1; n + 1]; n];
        fn dp(i: usize, m: usize, n: usize, suffix: &[i32], memo: &mut [Vec<i32>]) -> i32 {
            if i >= n {
                return 0;
            }
            if memo[i][m] != -1 {
                return memo[i][m];
            }
            let mut best = 0;
            let mut x = 1;
            while x <= 2 * m && i + x - 1 < n {
                let v = suffix[i] - dp(i + x, m.max(x), n, suffix, memo);
                best = best.max(v);
                x += 1;
            }
            memo[i][m] = best;
            best
        }
        dp(0, 1, n, &suffix, &mut memo)
    }
}
