// LeetCode 3282 - Reach End of Array With Max Score
// https://leetcode.com/problems/reach-end-of-array-with-max-score/

impl Solution {
    pub fn find_maximum_score(nums: Vec<i32>) -> i64 {
        let mut ans = 0i64;
        let mut max_v = 0;
        for i in 0..nums.len() - 1 {
            if nums[i] > max_v {
                max_v = nums[i];
            }
            ans += max_v as i64;
        }
        ans
    }
}
