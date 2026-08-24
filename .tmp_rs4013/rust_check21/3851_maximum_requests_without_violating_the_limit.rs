struct Solution;
// LeetCode 3851 - Maximum Requests Without Violating the Limit
// https://leetcode.com/problems/maximum-requests-without-violating-the-limit/

use std::collections::HashMap;

impl Solution {
    pub fn max_requests(requests: Vec<Vec<i32>>, k: i32, window: i32) -> i32 {
        let mut g: HashMap<i32, Vec<i32>> = HashMap::new();
        for r in &requests {
            g.entry(r[0]).or_default().push(r[1]);
        }
        let mut ans = requests.len() as i32;
        for ts in g.values_mut() {
            ts.sort_unstable();
            let mut kept = Vec::new();
            for &t in ts.iter() {
                while !kept.is_empty() && t - kept[0] > window {
                    kept.remove(0);
                }
                if (kept.len() as i32) < k {
                    kept.push(t);
                } else {
                    ans -= 1;
                }
            }
        }
        ans
    }
}
