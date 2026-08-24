struct Solution;
// LeetCode 3847 - Find the Score Difference in a Game
// https://leetcode.com/problems/find-the-score-difference-in-a-game/

impl Solution {
    pub fn score_difference(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut k = 1;
        for (i, &x) in nums.iter().enumerate() {
            if x % 2 != 0 {
                k = -k;
            }
            if i % 6 == 5 {
                k = -k;
            }
            ans += k * x;
        }
        ans
    }
}
