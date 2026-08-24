// LeetCode 2419 - Longest Subarray With Maximum Bitwise AND
// https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

impl Solution {
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        let mx = *nums.iter().max().unwrap();
        let mut ans = 0;
        let mut cur = 0;
        for x in nums {
            if x == mx {
                cur += 1;
                ans = ans.max(cur);
            } else {
                cur = 0;
            }
        }
        ans
    }
}
