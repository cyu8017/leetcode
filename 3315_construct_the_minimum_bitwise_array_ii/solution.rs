// LeetCode 3315 - Construct the Minimum Bitwise Array II
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

impl Solution {
    pub fn min_bitwise_array(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = vec![-1; nums.len()];
        for i in 0..nums.len() {
            let n = nums[i];
            if n == 2 {
                continue;
            }
            for b in 0..31 {
                if ((n >> b) & 1) == 0 {
                    continue;
                }
                let x = n ^ (1 << b);
                if (x | (x + 1)) == n {
                    ans[i] = x;
                    break;
                }
            }
        }
        ans
    }
}
