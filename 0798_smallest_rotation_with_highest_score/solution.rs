// LeetCode 0798 - Smallest Rotation with Highest Score
// https://leetcode.com/problems/smallest-rotation-with-highest-score/

impl Solution {
    pub fn best_rotation(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut change = vec![1i32; n];
        for i in 0..n {
            let idx = (i as i32 - nums[i] + 1 + n as i32) as usize % n;
            change[idx] -= 1;
        }
        for i in 1..n {
            change[i] += change[i - 1];
        }
        let mut best = 0;
        for i in 1..n {
            if change[i] > change[best] {
                best = i;
            }
        }
        best as i32
    }
}
