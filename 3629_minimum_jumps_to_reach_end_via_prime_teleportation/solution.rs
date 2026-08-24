// LeetCode 3629 - Minimum Jumps to Reach End via Prime Teleportation
// https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

use std::collections::HashMap;

impl Solution {
    pub fn min_jumps(nums: Vec<i32>) -> i32 {
        const MX: usize = 1_000_001;
        let mut fac = vec![Vec::new(); MX];
        for i in 2..MX {
            if fac[i].is_empty() {
                let mut j = i;
                while j < MX {
                    fac[j].push(i as i32);
                    j += i;
                }
            }
        }
        let n = nums.len();
        let mut g: HashMap<i32, Vec<usize>> = HashMap::new();
        for i in 0..n {
            for &p in &fac[nums[i] as usize] {
                g.entry(p).or_default().push(i);
            }
        }
        let mut ans = 0;
        let mut vis = vec![false; n];
        vis[0] = true;
        let mut q = vec![0usize];
        loop {
            let mut nq = Vec::new();
            for &i in &q {
                if i == n - 1 {
                    return ans;
                }
                let mut idx = g.remove(&nums[i]).unwrap_or_default();
                idx.push(i + 1);
                if i > 0 {
                    idx.push(i - 1);
                }
                for j in idx {
                    if j < n && !vis[j] {
                        vis[j] = true;
                        nq.push(j);
                    }
                }
            }
            q = nq;
            ans += 1;
        }
    }
}
