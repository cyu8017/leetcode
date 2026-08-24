// LeetCode 3960 - Frequency Balance Subarray
// https://leetcode.com/problems/frequency-balance-subarray/

use std::collections::HashMap;

impl Solution {
    pub fn get_length(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 1;
        for l in 0..n {
            let mut cnt: HashMap<i32, i32> = HashMap::new();
            let mut freq: HashMap<i32, i32> = HashMap::new();
            for r in l..n {
                let x = nums[r];
                let c = *cnt.get(&x).unwrap_or(&0);
                if let Some(f) = freq.get_mut(&c) {
                    *f -= 1;
                    if *f == 0 {
                        freq.remove(&c);
                    }
                }
                cnt.insert(x, c + 1);
                *freq.entry(cnt[&x]).or_insert(0) += 1;
                let cx = cnt[&x];
                if cnt.len() == 1
                    || (freq.len() == 2
                        && (*freq.get(&(cx * 2)).unwrap_or(&0) > 0
                            || (cx % 2 == 0 && *freq.get(&(cx / 2)).unwrap_or(&0) > 0)))
                {
                    ans = ans.max((r - l + 1) as i32);
                }
            }
        }
        ans
    }
}
