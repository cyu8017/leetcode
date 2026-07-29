// LeetCode 1066 - Campus Bikes II
// https://leetcode.com/problems/campus-bikes-ii/

impl Solution {
    pub fn assign_bikes(workers: Vec<Vec<i32>>, bikes: Vec<Vec<i32>>) -> i32 {
        let m = bikes.len();
        let n = workers.len();
        let mut memo = vec![vec![-1i32; 1 << m]; n + 1];
        Self::dp(0, 0, &workers, &bikes, &mut memo)
    }

    fn dp(
        i: usize,
        mask: usize,
        workers: &[Vec<i32>],
        bikes: &[Vec<i32>],
        memo: &mut [Vec<i32>],
    ) -> i32 {
        if i == workers.len() {
            return 0;
        }
        if memo[i][mask] != -1 {
            return memo[i][mask];
        }
        let mut best = i32::MAX;
        let wx = workers[i][0];
        let wy = workers[i][1];
        for b in 0..bikes.len() {
            if mask & (1 << b) != 0 {
                continue;
            }
            let dist = (wx - bikes[b][0]).abs() + (wy - bikes[b][1]).abs();
            best = best.min(dist + Self::dp(i + 1, mask | (1 << b), workers, bikes, memo));
        }
        memo[i][mask] = best;
        best
    }
}
