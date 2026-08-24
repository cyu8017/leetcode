// LeetCode 3690 - Split and Merge Array Transformation
// https://leetcode.com/problems/split-and-merge-array-transformation/

use std::collections::HashSet;

impl Solution {
    pub fn min_split_merge(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n = nums1.len();
        let to_arr = |nums: &[i32]| -> [i32; 6] {
            let mut t = [0; 6];
            for i in 0..n {
                t[i] = nums[i];
            }
            t
        };
        let start = to_arr(&nums1);
        let target = to_arr(&nums2);
        let mut vis = HashSet::new();
        vis.insert(start);
        let mut q = vec![start];
        let mut ans = 0;
        loop {
            let mut nq = Vec::new();
            for cur in &q {
                if *cur == target {
                    return ans;
                }
                for l in 0..n {
                    for r in l..n {
                        let mut remain = Vec::new();
                        let mut sub = Vec::new();
                        for i in 0..l {
                            remain.push(cur[i]);
                        }
                        for i in r + 1..n {
                            remain.push(cur[i]);
                        }
                        for i in l..=r {
                            sub.push(cur[i]);
                        }
                        for pos in 0..=remain.len() {
                            let mut nxt_slice = Vec::new();
                            nxt_slice.extend_from_slice(&remain[..pos]);
                            nxt_slice.extend_from_slice(&sub);
                            nxt_slice.extend_from_slice(&remain[pos..]);
                            let nxt = to_arr(&nxt_slice);
                            if vis.insert(nxt) {
                                nq.push(nxt);
                            }
                        }
                    }
                }
            }
            q = nq;
            ans += 1;
        }
    }
}
