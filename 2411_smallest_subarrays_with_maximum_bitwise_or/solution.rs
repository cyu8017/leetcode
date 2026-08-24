// LeetCode 2411 - Smallest Subarrays With Maximum Bitwise OR
// https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

impl Solution {
    pub fn smallest_subarrays(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut ans = vec![0; n];
        let mut last = [-1i32; 32];
        for i in (0..n).rev() {
            for b in 0..32 {
                if (nums[i] >> b) & 1 == 1 {
                    last[b] = i as i32;
                }
            }
            let mut far = i as i32;
            for b in 0..32 {
                far = far.max(last[b]);
            }
            ans[i] = far - i as i32 + 1;
        }
        ans
    }
}
