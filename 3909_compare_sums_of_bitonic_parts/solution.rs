// LeetCode 3909 - Compare Sums of Bitonic Parts
// https://leetcode.com/problems/compare-sums-of-bitonic-parts/

impl Solution {
    pub fn compare_bitonic_sums(nums: Vec<i32>) -> i32 {
        let mut l = nums[0] as i64;
        let mut r: i64 = nums.iter().map(|&x| x as i64).sum();
        for i in 1..nums.len() {
            if nums[i - 1] > nums[i] {
                break;
            }
            l += nums[i] as i64;
            r -= nums[i - 1] as i64;
        }
        if l == r {
            -1
        } else if l > r {
            0
        } else {
            1
        }
    }
}
