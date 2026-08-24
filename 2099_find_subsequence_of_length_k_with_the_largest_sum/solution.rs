// LeetCode 2099 - Find Subsequence of Length K With the Largest Sum
// https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

impl Solution {
    pub fn max_subsequence(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        let mut arr: Vec<(i32, usize)> = nums.iter().copied().enumerate().map(|(i, v)| (v, i)).collect();
        arr.sort_by(|a, b| b.0.cmp(&a.0));
        let mut idx: Vec<usize> = arr[..k].iter().map(|p| p.1).collect();
        idx.sort_unstable();
        idx.into_iter().map(|i| nums[i]).collect()
    }
}
