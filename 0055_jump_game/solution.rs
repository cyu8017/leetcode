// LeetCode 0055 - Jump Game
// https://leetcode.com/problems/jump-game/

impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let mut farthest = 0;

        for (i, jump) in nums.iter().enumerate() {
            if i > farthest {
                return false;
            }
            farthest = farthest.max(i + *jump as usize);
        }

        true
    }
}
