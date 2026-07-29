// LeetCode 1090 - Largest Values From Labels
// https://leetcode.com/problems/largest-values-from-labels/

use std::collections::HashMap;

impl Solution {
    pub fn largest_vals_from_labels(
        values: Vec<i32>,
        labels: Vec<i32>,
        num_wanted: i32,
        use_limit: i32,
    ) -> i32 {
        let mut items: Vec<(i32, i32)> = values.into_iter().zip(labels).collect();
        items.sort_unstable_by(|a, b| b.0.cmp(&a.0));
        let mut used: HashMap<i32, i32> = HashMap::new();
        let mut ans = 0;
        let mut taken = 0;
        for (value, label) in items {
            if taken == num_wanted {
                break;
            }
            let count = used.entry(label).or_insert(0);
            if *count < use_limit {
                *count += 1;
                ans += value;
                taken += 1;
            }
        }
        ans
    }
}
