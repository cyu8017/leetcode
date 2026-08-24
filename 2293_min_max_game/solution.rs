// LeetCode 2293 - Min Max Game
// https://leetcode.com/problems/min-max-game/

impl Solution {
    pub fn min_max_game(mut nums: Vec<i32>) -> i32 {
        while nums.len() > 1 {
            let next: Vec<i32> = (0..nums.len() / 2)
                .map(|i| {
                    if i % 2 == 0 {
                        nums[2 * i].min(nums[2 * i + 1])
                    } else {
                        nums[2 * i].max(nums[2 * i + 1])
                    }
                })
                .collect();
            nums = next;
        }
        nums[0]
    }
}
