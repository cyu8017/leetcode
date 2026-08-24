struct Solution;
fn main() {}

// LeetCode 2747 - Count Zero Request Servers
// https://leetcode.com/problems/count-zero-request-servers/

use std::collections::HashMap;

impl Solution {
    pub fn count_servers(n: i32, mut logs: Vec<Vec<i32>>, x: i32, queries: Vec<i32>) -> Vec<i32> {
        logs.sort_unstable_by_key(|a| a[1]);
        let mut qs: Vec<(i32, usize)> = queries.iter().enumerate().map(|(i, &t)| (t, i)).collect();
        qs.sort_unstable_by_key(|a| a.0);
        let mut ans = vec![0; queries.len()];
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        let mut active = 0;
        let mut l = 0;
        let mut r = 0;
        for &(t, qi) in &qs {
            while r < logs.len() && logs[r][1] <= t {
                let id = logs[r][0];
                let e = cnt.entry(id).or_insert(0);
                if *e == 0 {
                    active += 1;
                }
                *e += 1;
                r += 1;
            }
            while l < r && logs[l][1] < t - x {
                let id = logs[l][0];
                if let Some(e) = cnt.get_mut(&id) {
                    *e -= 1;
                    if *e == 0 {
                        active -= 1;
                    }
                }
                l += 1;
            }
            ans[qi] = n - active;
        }
        ans
    }
}
