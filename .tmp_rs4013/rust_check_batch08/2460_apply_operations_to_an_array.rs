struct Solution;
// LeetCode 2460 - Apply Operations to an Array
// https://leetcode.com/problems/apply-operations-to-an-array/

impl Solution {
    pub fn apply_operations(mut nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        for i in 0..n.saturating_sub(1) {
            if nums[i] == nums[i + 1] {
                nums[i] *= 2;
                nums[i + 1] = 0;
            }
        }
        let mut ans = vec![0; n];
        let mut j = 0;
        for x in nums {
            if x != 0 {
                ans[j] = x;
                j += 1;
            }
        }
        ans
    }
}

fn main() {}
