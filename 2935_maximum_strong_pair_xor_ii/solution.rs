// LeetCode 2935 - Maximum Strong Pair XOR II
// https://leetcode.com/problems/maximum-strong-pair-xor-ii/

impl Solution {
    pub fn maximum_strong_pair_xor(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let mut ans = 0;
        for i in 0..nums.len() {
            let x = nums[i];
            let mut j = i;
            while j < nums.len() && nums[j] <= 2 * x {
                let xorr = x ^ nums[j];
                if xorr > ans {
                    ans = xorr;
                }
                j += 1;
            }
        }
        ans
    }
}
