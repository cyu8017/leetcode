// LeetCode 1681 - Minimum Incompatibility
// https://leetcode.com/problems/minimum-incompatibility/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_incompatibility(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let size = n / k as usize;
        let full = (1 << n) - 1;
        let mut groups = HashMap::new();
        for mask in 0usize..(1 << n) {
            if mask.count_ones() as usize != size {
                continue;
            }
            let mut seen = [false; 17];
            let mut ok = true;
            let mut mn = i32::MAX;
            let mut mx = 0;
            let mut count = 0;
            for i in 0..n {
                if mask >> i & 1 == 0 {
                    continue;
                }
                let v = nums[i];
                if seen[v as usize] {
                    ok = false;
                    break;
                }
                seen[v as usize] = true;
                count += 1;
                mn = mn.min(v);
                mx = mx.max(v);
            }
            if ok && count == size {
                groups.insert(mask, mx - mn);
            }
        }
        const INF: i32 = 1_000_000_000;
        let mut memo = HashMap::new();
        fn dp(
            mask: usize,
            n: usize,
            full: usize,
            groups: &HashMap<usize, i32>,
            memo: &mut HashMap<usize, i32>,
        ) -> i32 {
            if mask == full {
                return 0;
            }
            if let Some(&v) = memo.get(&mask) {
                return v;
            }
            let mut first = 0;
            for i in 0..n {
                if mask >> i & 1 == 0 {
                    first = i;
                    break;
                }
            }
            let mut best = INF;
            for (&g, &c) in groups {
                if g >> first & 1 != 0 && g & mask == 0 {
                    best = best.min(c + dp(mask | g, n, full, groups, memo));
                }
            }
            memo.insert(mask, best);
            best
        }
        let ans = dp(0, n, full, &groups, &mut memo);
        if ans >= INF {
            -1
        } else {
            ans
        }
    }
}
