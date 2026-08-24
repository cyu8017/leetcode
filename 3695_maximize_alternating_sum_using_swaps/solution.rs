// LeetCode 3695 - Maximize Alternating Sum Using Swaps
// https://leetcode.com/problems/maximize-alternating-sum-using-swaps/

use std::collections::HashMap;

impl Solution {
    pub fn max_alternating_sum(nums: Vec<i32>, swaps: Vec<Vec<i32>>) -> i64 {
        let n = nums.len();
        let mut parent: Vec<usize> = (0..n).collect();
        fn find(parent: &mut [usize], x: usize) -> usize {
            if parent[x] != x {
                parent[x] = find(parent, parent[x]);
            }
            parent[x]
        }
        for s in swaps {
            let a = find(&mut parent, s[0] as usize);
            let b = find(&mut parent, s[1] as usize);
            if a != b {
                parent[a] = b;
            }
        }
        let mut comp_vals: HashMap<usize, Vec<i32>> = HashMap::new();
        let mut comp_idx: HashMap<usize, Vec<usize>> = HashMap::new();
        for i in 0..n {
            let r = find(&mut parent, i);
            comp_vals.entry(r).or_default().push(nums[i]);
            comp_idx.entry(r).or_default().push(i);
        }
        let mut arr = vec![0; n];
        for (r, mut vals) in comp_vals {
            let idxs = &comp_idx[&r];
            vals.sort_unstable_by(|a, b| b.cmp(a));
            let mut even = Vec::new();
            let mut odd = Vec::new();
            for &i in idxs {
                if i % 2 == 0 {
                    even.push(i);
                } else {
                    odd.push(i);
                }
            }
            even.sort_unstable();
            odd.sort_unstable();
            let mut ei = 0;
            for v in vals {
                if ei < even.len() {
                    arr[even[ei]] = v;
                } else {
                    arr[odd[ei - even.len()]] = v;
                }
                ei += 1;
            }
        }
        let mut ans = 0i64;
        for i in 0..n {
            if i % 2 == 0 {
                ans += arr[i] as i64;
            } else {
                ans -= arr[i] as i64;
            }
        }
        ans
    }
}
