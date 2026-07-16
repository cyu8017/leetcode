// LeetCode 0473 - Matchsticks to Square
// https://leetcode.com/problems/matchsticks-to-square/

impl Solution {
    fn dfs(index: usize, side: i32, matchsticks: &[i32], sides: &mut [i32; 4]) -> bool {
        if index == matchsticks.len() {
            return sides[0] == side && sides[1] == side && sides[2] == side && sides[3] == side;
        }

        let length = matchsticks[index];
        for side_index in 0..4 {
            if sides[side_index] + length > side {
                continue;
            }
            if side_index > 0 && sides[side_index] == sides[side_index - 1] {
                continue;
            }
            sides[side_index] += length;
            if Self::dfs(index + 1, side, matchsticks, sides) {
                return true;
            }
            sides[side_index] -= length;
        }
        false
    }

    pub fn makesquare(matchsticks: Vec<i32>) -> bool {
        if matchsticks.is_empty() {
            return false;
        }
        let total: i32 = matchsticks.iter().sum();
        if total % 4 != 0 {
            return false;
        }
        let side = total / 4;
        let mut matchsticks = matchsticks;
        matchsticks.sort_unstable_by(|left, right| right.cmp(left));
        let mut sides = [0; 4];
        Self::dfs(0, side, &matchsticks, &mut sides)
    }
}
