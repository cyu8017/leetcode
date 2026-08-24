// LeetCode 2948 - Make Lexicographically Smallest Array by Swapping Elements
// https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

impl Solution {
    pub fn lexicographically_smallest_array(nums: Vec<i32>, limit: i32) -> Vec<i32> {
        let n = nums.len();
        let mut idx: Vec<usize> = (0..n).collect();
        idx.sort_by_key(|&i| nums[i]);
        let mut ans = vec![0; n];
        let mut i = 0;
        while i < n {
            let mut j = i + 1;
            while j < n && nums[idx[j]] - nums[idx[j - 1]] <= limit {
                j += 1;
            }
            let mut group_idx = idx[i..j].to_vec();
            group_idx.sort_unstable();
            for t in 0..(j - i) {
                ans[group_idx[t]] = nums[idx[i + t]];
            }
            i = j;
        }
        ans
    }
}
