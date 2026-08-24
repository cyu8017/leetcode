// LeetCode 2354 - Number of Excellent Pairs
// https://leetcode.com/problems/number-of-excellent-pairs/

use std::collections::HashSet;

impl Solution {
    pub fn count_excellent_pairs(nums: Vec<i32>, k: i32) -> i64 {
        let uniq: HashSet<i32> = nums.into_iter().collect();
        let mut cnt = [0i64; 32];
        for x in uniq {
            cnt[x.count_ones() as usize] += 1;
        }
        let mut ans = 0i64;
        for i in 0..32 {
            for j in 0..32 {
                if i + j >= k as usize {
                    ans += cnt[i] * cnt[j];
                }
            }
        }
        ans
    }
}
