// LeetCode 1671 - Minimum Number of Removals to Make Mountain Array
// https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

impl Solution {
    pub fn minimum_mountain_removals(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let lis = |a: &[i32]| -> Vec<i32> {
            let mut d = Vec::new();
            let mut out = Vec::with_capacity(a.len());
            for &x in a {
                let i = d.partition_point(|&y| y < x);
                if i == d.len() {
                    d.push(x);
                } else {
                    d[i] = x;
                }
                out.push((i + 1) as i32);
            }
            out
        };
        let l = lis(&nums);
        let rev: Vec<i32> = nums.iter().copied().rev().collect();
        let r: Vec<i32> = lis(&rev).into_iter().rev().collect();
        let mut best = 0;
        for i in 0..n {
            if l[i] > 1 && r[i] > 1 {
                best = best.max(l[i] + r[i] - 1);
            }
        }
        n as i32 - best
    }
}
