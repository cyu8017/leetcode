// LeetCode 2155 - All Divisions With the Highest Score of a Binary Array
// https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

impl Solution {
    pub fn max_score_indices(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let total1: i32 = nums.iter().sum();
        let mut best = total1;
        let mut left0 = 0;
        let mut right1 = total1;
        let mut ans = vec![0];
        for i in 0..n {
            if nums[i] == 0 {
                left0 += 1;
            } else {
                right1 -= 1;
            }
            let score = left0 + right1;
            if score > best {
                best = score;
                ans = vec![i as i32 + 1];
            } else if score == best {
                ans.push(i as i32 + 1);
            }
        }
        ans
    }
}
