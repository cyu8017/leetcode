// LeetCode 2107 - Number of Unique Flavors After Sharing K Candies
// https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/

use std::collections::HashMap;

impl Solution {
    pub fn share_candies(candies: Vec<i32>, k: i32) -> i32 {
        let n = candies.len();
        let k = k as usize;
        let mut freq = HashMap::new();
        for &c in &candies {
            *freq.entry(c).or_insert(0) += 1;
        }
        if k == 0 {
            return freq.len() as i32;
        }
        for i in 0..k {
            let e = freq.get_mut(&candies[i]).unwrap();
            *e -= 1;
            if *e == 0 {
                freq.remove(&candies[i]);
            }
        }
        let mut ans = freq.len() as i32;
        for i in k..n {
            *freq.entry(candies[i - k]).or_insert(0) += 1;
            let e = freq.get_mut(&candies[i]).unwrap();
            *e -= 1;
            if *e == 0 {
                freq.remove(&candies[i]);
            }
            ans = ans.max(freq.len() as i32);
        }
        ans
    }
}
