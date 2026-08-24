// LeetCode 3221 - Maximum Array Hopping Score II
// https://leetcode.com/problems/maximum-array-hopping-score-ii/

impl Solution {
    pub fn max_score(nums: Vec<i32>) -> i64 {
        let mut stk = Vec::new();
        for i in 0..nums.len() {
            while !stk.is_empty() && nums[*stk.last().unwrap()] <= nums[i] {
                stk.pop();
            }
            stk.push(i);
        }
        let mut ans = 0i64;
        let mut i = 0;
        for j in stk {
            ans += (j - i) as i64 * nums[j] as i64;
            i = j;
        }
        ans
    }
}
