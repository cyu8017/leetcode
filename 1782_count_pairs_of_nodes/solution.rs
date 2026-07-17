// LeetCode 1782 - Count Pairs Of Nodes
// https://leetcode.com/problems/count-pairs-of-nodes/

use std::collections::HashMap;

impl Solution {
    pub fn count_pairs(n: i32, edges: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
        let n = n as usize;
        let mut deg = vec![0i32; n + 1];
        let mut shared: HashMap<(usize, usize), i32> = HashMap::new();
        for edge in &edges {
            let mut a = edge[0] as usize;
            let mut b = edge[1] as usize;
            if a > b {
                std::mem::swap(&mut a, &mut b);
            }
            deg[a] += 1;
            deg[b] += 1;
            *shared.entry((a, b)).or_insert(0) += 1;
        }
        let mut sorted_deg = deg[1..].to_vec();
        sorted_deg.sort_unstable();
        let mut ans = Vec::with_capacity(queries.len());
        for &q in &queries {
            let mut res: i64 = 0;
            let mut left = 0usize;
            let mut right = n - 1;
            while left < right {
                if sorted_deg[left] + sorted_deg[right] > q {
                    res += (right - left) as i64;
                    right -= 1;
                } else {
                    left += 1;
                }
            }
            for (&(a, b), &count) in &shared {
                let sum = deg[a] + deg[b];
                if sum > q && q >= sum - count {
                    res -= 1;
                }
            }
            ans.push(res as i32);
        }
        ans
    }
}
