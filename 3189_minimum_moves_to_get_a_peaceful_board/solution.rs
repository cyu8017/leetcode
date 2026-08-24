// LeetCode 3189 - Minimum Moves to Get a Peaceful Board
// https://leetcode.com/problems/minimum-moves-to-get-a-peaceful-board/

impl Solution {
    pub fn min_moves(mut rooks: Vec<Vec<i32>>) -> i32 {
        let mut ans = 0;
        rooks.sort_unstable_by_key(|a| a[0]);
        for (i, r) in rooks.iter().enumerate() {
            ans += (r[0] - i as i32).abs();
        }
        rooks.sort_unstable_by_key(|a| a[1]);
        for (j, r) in rooks.iter().enumerate() {
            ans += (r[1] - j as i32).abs();
        }
        ans
    }
}
