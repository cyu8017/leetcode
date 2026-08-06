// LeetCode 1217 - Minimum Cost to Move Chips to The Same Position
// https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

impl Solution {
    pub fn min_cost_to_move_chips(position: Vec<i32>) -> i32 {
        let odd = position.iter().filter(|&&x| x & 1 == 1).count() as i32;
        let even = position.len() as i32 - odd;
        odd.min(even)
    }
}
