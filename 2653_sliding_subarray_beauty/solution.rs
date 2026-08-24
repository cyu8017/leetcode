// LeetCode 2653 - Sliding Subarray Beauty
// https://leetcode.com/problems/sliding-subarray-beauty/

impl Solution {
    pub fn get_subarray_beauty(nums: Vec<i32>, k: i32, x: i32) -> Vec<i32> {
        let mut freq = [0i32; 101];
        let k = k as usize;
        let mut ans = vec![0; nums.len() - k + 1];
        for i in 0..nums.len() {
            freq[(nums[i] + 50) as usize] += 1;
            if i >= k {
                freq[(nums[i - k] + 50) as usize] -= 1;
            }
            if i >= k - 1 {
                let mut need = x;
                let mut val = 0;
                for j in 0..50 {
                    need -= freq[j];
                    if need <= 0 {
                        val = j as i32 - 50;
                        break;
                    }
                }
                ans[i - k + 1] = val;
            }
        }
        ans
    }
}
