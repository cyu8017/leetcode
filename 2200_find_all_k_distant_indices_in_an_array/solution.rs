// LeetCode 2200 - Find All K-Distant Indices in an Array
// https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

impl Solution {
    pub fn find_k_distant_indices(nums: Vec<i32>, key: i32, k: i32) -> Vec<i32> {
        let n = nums.len() as i32;
        let mut mark = vec![false; n as usize];
        for i in 0..n {
            if nums[i as usize] == key {
                let l = 0.max(i - k);
                let r = (n - 1).min(i + k);
                for j in l..=r {
                    mark[j as usize] = true;
                }
            }
        }
        (0..n).filter(|&i| mark[i as usize]).collect()
    }
}
