// LeetCode 1040 - Moving Stones Until Consecutive II
// https://leetcode.com/problems/moving-stones-until-consecutive-ii/

impl Solution {
    pub fn num_moves_stones_ii(mut stones: Vec<i32>) -> Vec<i32> {
        stones.sort_unstable();
        let n = stones.len();
        let max_moves = (stones[n - 1] - stones[1] - n as i32 + 2)
            .max(stones[n - 2] - stones[0] - n as i32 + 2);
        let mut min_moves = max_moves;
        let mut i = 0;
        for j in 0..n {
            while stones[j] - stones[i] + 1 > n as i32 {
                i += 1;
            }
            let inside = j - i + 1;
            if inside == n - 1 && stones[j] - stones[i] + 1 == n as i32 - 1 {
                min_moves = min_moves.min(2);
            } else {
                min_moves = min_moves.min((n - inside) as i32);
            }
        }
        vec![min_moves, max_moves]
    }
}
