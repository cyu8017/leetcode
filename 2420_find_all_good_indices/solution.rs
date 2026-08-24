// LeetCode 2420 - Find All Good Indices
// https://leetcode.com/problems/find-all-good-indices/

impl Solution {
    pub fn good_indices(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let k = k as usize;
        let mut dec = vec![0; n];
        let mut inc = vec![0; n];
        dec[0] = 1;
        for i in 1..n {
            dec[i] = if nums[i] <= nums[i - 1] {
                dec[i - 1] + 1
            } else {
                1
            };
        }
        inc[n - 1] = 1;
        for i in (0..n - 1).rev() {
            inc[i] = if nums[i] <= nums[i + 1] {
                inc[i + 1] + 1
            } else {
                1
            };
        }
        let mut ans = Vec::new();
        if n > 2 * k {
            for i in k..n - k {
                if dec[i - 1] >= k && inc[i + 1] >= k {
                    ans.push(i as i32);
                }
            }
        }
        ans
    }
}
