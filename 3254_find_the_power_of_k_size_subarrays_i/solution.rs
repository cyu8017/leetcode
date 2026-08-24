// LeetCode 3254 - Find the Power of K-Size Subarrays I
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

impl Solution {
    pub fn results_array(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let k = k as usize;
        let mut ans = vec![0; n - k + 1];
        for i in 0..=n - k {
            let mut ok = true;
            for j in i + 1..i + k {
                if nums[j] != nums[j - 1] + 1 {
                    ok = false;
                    break;
                }
            }
            ans[i] = if ok { nums[i + k - 1] } else { -1 };
        }
        ans
    }
}
