// LeetCode 2597 - The Number of Beautiful Subsets
// https://leetcode.com/problems/the-number-of-beautiful-subsets/

use std::collections::HashMap;

impl Solution {
    pub fn beautiful_subsets(nums: Vec<i32>, k: i32) -> i32 {
        let mut freq = HashMap::new();
        for x in nums {
            *freq.entry(x).or_insert(0) += 1;
        }
        let mut groups: HashMap<i32, Vec<i32>> = HashMap::new();
        for &x in freq.keys() {
            groups.entry(x % k).or_default().push(x);
        }
        let mut ans = 1;
        for vals in groups.values_mut() {
            vals.sort_unstable();
            let mut prev_take = 0;
            let mut prev_skip = 1;
            let mut prev_val = i32::MIN / 2;
            for &v in vals.iter() {
                let mut ways = 1;
                for _ in 0..freq[&v] {
                    ways *= 2;
                }
                ways -= 1;
                let skip = prev_take + prev_skip;
                let mut take = ways * prev_skip;
                if prev_val + k != v {
                    take += ways * prev_take;
                }
                prev_take = take;
                prev_skip = skip;
                prev_val = v;
            }
            ans *= prev_take + prev_skip;
        }
        ans - 1
    }
}
