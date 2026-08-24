// LeetCode 3693 - Climbing Stairs II
// https://leetcode.com/problems/climbing-stairs-ii/

impl Solution {
    pub fn climb_stairs(n: i32, costs: Vec<i32>) -> i32 {
        let n = n as usize;
        let inf = 1_000_000_000;
        let mut f = vec![inf; n + 1];
        f[0] = 0;
        for i in 1..=n {
            let x = costs[i - 1];
            let start = if i >= 3 { i - 3 } else { 0 };
            for j in start..i {
                let d = (i - j) as i32;
                f[i] = f[i].min(f[j] + x + d * d);
            }
        }
        f[n]
    }
}
