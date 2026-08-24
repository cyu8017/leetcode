// LeetCode 2640 - Find the Score of All Prefixes of an Array
// https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

impl Solution {
    pub fn find_prefix_score(nums: Vec<i32>) -> Vec<i64> {
        let mut ans = vec![0i64; nums.len()];
        let mut mx = 0;
        let mut sum = 0i64;
        for i in 0..nums.len() {
            if nums[i] > mx {
                mx = nums[i];
            }
            sum += nums[i] as i64 + mx as i64;
            ans[i] = sum;
        }
        ans
    }
}
