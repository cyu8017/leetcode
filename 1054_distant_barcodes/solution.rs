// LeetCode 1054 - Distant Barcodes
// https://leetcode.com/problems/distant-barcodes/

use std::collections::HashMap;

impl Solution {
    pub fn rearrange_barcodes(barcodes: Vec<i32>) -> Vec<i32> {
        let mut count: HashMap<i32, i32> = HashMap::new();
        for &b in &barcodes {
            *count.entry(b).or_insert(0) += 1;
        }
        let mut items: Vec<(i32, i32)> = count.into_iter().collect();
        items.sort_by(|a, b| b.1.cmp(&a.1));
        let n = barcodes.len();
        let mut ans = vec![0; n];
        let mut i = 0;
        for (value, freq) in items {
            for _ in 0..freq {
                ans[i] = value;
                i += 2;
                if i >= n {
                    i = 1;
                }
            }
        }
        ans
    }
}
