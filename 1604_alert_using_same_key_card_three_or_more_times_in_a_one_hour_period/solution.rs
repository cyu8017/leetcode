// LeetCode 1604 - Alert Using Same Key-Card Three or More Times in a One Hour Period
// https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

use std::collections::HashMap;

impl Solution {
    pub fn alert_names(key_name: Vec<String>, key_time: Vec<String>) -> Vec<String> {
        let mut times: HashMap<String, Vec<i32>> = HashMap::new();
        for (name, t) in key_name.into_iter().zip(key_time) {
            let parts: Vec<_> = t.split(':').collect();
            let h: i32 = parts[0].parse().unwrap();
            let m: i32 = parts[1].parse().unwrap();
            times.entry(name).or_default().push(h * 60 + m);
        }
        let mut ans = Vec::new();
        for (name, mut a) in times {
            a.sort_unstable();
            if a.windows(3).any(|w| w[2] - w[0] <= 60) {
                ans.push(name);
            }
        }
        ans.sort();
        ans
    }
}
