// LeetCode 2285 - Maximum Total Importance of Roads
// https://leetcode.com/problems/maximum-total-importance-of-roads/

impl Solution {
    pub fn maximum_importance(n: i32, roads: Vec<Vec<i32>>) -> i64 {
        let mut deg = vec![0i32; n as usize];
        for r in roads {
            deg[r[0] as usize] += 1;
            deg[r[1] as usize] += 1;
        }
        deg.sort_unstable();
        let mut ans = 0i64;
        for i in 0..n as usize {
            ans += deg[i] as i64 * (i as i64 + 1);
        }
        ans
    }
}
