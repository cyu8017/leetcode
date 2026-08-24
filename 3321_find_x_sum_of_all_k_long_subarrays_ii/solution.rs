// LeetCode 3321 - Find X-Sum of All K-Long Subarrays II
// https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/

use std::collections::HashMap;

impl Solution {
    pub fn find_x_sum(nums: Vec<i32>, k: i32, x: i32) -> Vec<i64> {
        let n = nums.len();
        let k = k as usize;
        let x = x as usize;
        let mut ans = vec![0i64; n - k + 1];
        for i in 0..=n - k {
            let mut freq: HashMap<i32, i32> = HashMap::new();
            for j in i..i + k {
                *freq.entry(nums[j]).or_insert(0) += 1;
            }
            let mut arr: Vec<(i32, i32)> = freq.iter().map(|(&v, &f)| (v, f)).collect();
            for a in 0..arr.len() {
                for b in a + 1..arr.len() {
                    if arr[b].1 > arr[a].1 || (arr[b].1 == arr[a].1 && arr[b].0 > arr[a].0) {
                        arr.swap(a, b);
                    }
                }
            }
            let lim = x.min(arr.len());
            let mut keep = HashMap::new();
            for t in 0..lim {
                keep.insert(arr[t].0, true);
            }
            let mut sum = 0i64;
            for j in i..i + k {
                if keep.contains_key(&nums[j]) {
                    sum += nums[j] as i64;
                }
            }
            ans[i] = sum;
        }
        ans
    }
}
