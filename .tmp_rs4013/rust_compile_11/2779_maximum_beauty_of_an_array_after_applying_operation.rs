struct Solution;
fn main() {}

// LeetCode 2779 - Maximum Beauty of an Array After Applying Operation
// https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

impl Solution {
    pub fn maximum_beauty(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort_unstable();
        let mut ans = 0;
        let mut left = 0;
        for right in 0..nums.len() {
            while nums[right] - nums[left] > 2 * k {
                left += 1;
            }
            ans = ans.max((right - left + 1) as i32);
        }
        ans
    }
}
