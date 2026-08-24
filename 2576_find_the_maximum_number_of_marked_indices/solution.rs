// LeetCode 2576 - Find the Maximum Number of Marked Indices
// https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/

impl Solution {
    pub fn max_num_of_marked_indices(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let n = nums.len();
        let mut i = 0;
        let mut ans = 0;
        for j in (n + 1) / 2..n {
            if 2 * nums[i] <= nums[j] {
                ans += 2;
                i += 1;
            }
        }
        ans
    }
}
