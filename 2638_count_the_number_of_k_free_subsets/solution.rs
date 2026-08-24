// LeetCode 2638 - Count the Number of K-Free Subsets
// https://leetcode.com/problems/count-the-number-of-k-free-subsets/

use std::collections::HashMap;

impl Solution {
    pub fn count_the_num_of_k_free_subsets(mut nums: Vec<i32>, k: i32) -> i64 {
        nums.sort_unstable();
        let mut groups: HashMap<i32, Vec<i32>> = HashMap::new();
        for x in nums {
            groups.entry(x % k).or_default().push(x);
        }
        let mut ans = 1i64;
        for g in groups.values() {
            let mut prev_val = -1;
            let mut prev_take = 0i64;
            let mut prev_skip = 1i64;
            for &v in g {
                let skip = prev_take + prev_skip;
                let take = if prev_val + k == v {
                    prev_skip
                } else {
                    prev_take + prev_skip
                };
                prev_take = take;
                prev_skip = skip;
                prev_val = v;
            }
            ans *= prev_take + prev_skip;
        }
        ans
    }
}
