struct Solution;
fn main() {}

// LeetCode 2765 - Longest Alternating Subarray
// https://leetcode.com/problems/longest-alternating-subarray/

impl Solution {
    pub fn alternating_subarray(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = -1;
        for i in 0..n {
            for j in i + 1..n {
                let expect = if (j - i) % 2 == 0 { -1 } else { 1 };
                if nums[j] - nums[j - 1] != expect {
                    break;
                }
                if nums[i + 1] - nums[i] != 1 {
                    break;
                }
                ans = ans.max((j - i + 1) as i32);
            }
        }
        ans
    }
}
