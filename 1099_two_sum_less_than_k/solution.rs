// LeetCode 1099 - Two Sum Less Than K
// https://leetcode.com/problems/two-sum-less-than-k/

impl Solution {
    pub fn two_sum_less_than_k(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort_unstable();
        let mut lo = 0usize;
        let mut hi = nums.len() - 1;
        let mut ans = -1;
        while lo < hi {
            let total = nums[lo] + nums[hi];
            if total < k {
                ans = ans.max(total);
                lo += 1;
            } else {
                hi -= 1;
            }
        }
        ans
    }
}
