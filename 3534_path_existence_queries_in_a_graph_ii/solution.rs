// LeetCode 3534 - Path Existence Queries in a Graph II
// https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/

impl Solution {
    pub fn path_existence_queries(n: i32, nums: Vec<i32>, max_diff: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut pairs: Vec<(i32, usize)> = (0..n).map(|i| (nums[i], i)).collect();
        pairs.sort();
        let m = 20;
        let mut f = vec![vec![0usize; m]; n];
        let mut r = n as i32 - 1;
        for l in (0..n).rev() {
            while pairs[r as usize].0 - pairs[l].0 > max_diff {
                r -= 1;
            }
            let i = pairs[l].1;
            let j = pairs[r as usize].1;
            f[i][0] = j;
            for k in 1..m {
                f[i][k] = f[f[i][k - 1]][k - 1];
            }
        }
        let mut ans = Vec::new();
        for q in queries {
            let mut i = q[0] as usize;
            let mut j = q[1] as usize;
            if nums[i] > nums[j] {
                std::mem::swap(&mut i, &mut j);
            }
            if i == j {
                ans.push(0);
                continue;
            }
            if nums[i] == nums[j] {
                ans.push(1);
                continue;
            }
            let mut d = 0;
            for k in (0..m).rev() {
                if nums[f[i][k]] < nums[j] {
                    d |= 1 << k;
                    i = f[i][k];
                }
            }
            if nums[f[i][0]] < nums[j] {
                ans.push(-1);
            } else {
                ans.push(d + 1);
            }
        }
        ans
    }
}
