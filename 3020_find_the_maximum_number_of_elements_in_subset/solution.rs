// LeetCode 3020 - Find the Maximum Number of Elements in Subset
// https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

use std::collections::HashMap;

impl Solution {
    pub fn maximum_length(nums: Vec<i32>) -> i32 {
        let mut cnt: HashMap<i64, i32> = HashMap::new();
        for x in nums {
            *cnt.entry(x as i64).or_insert(0) += 1;
        }
        let mut ans = {
            let c1 = *cnt.get(&1).unwrap_or(&0);
            c1 - ((c1 % 2) ^ 1)
        };
        cnt.remove(&1);
        let keys: Vec<i64> = cnt.keys().copied().collect();
        for mut x in keys {
            let mut t = 0;
            while *cnt.get(&x).unwrap_or(&0) > 1 {
                if x > i64::MAX / x {
                    break;
                }
                x = x * x;
                t += 2;
            }
            if *cnt.get(&x).unwrap_or(&0) > 0 {
                t += 1;
            } else {
                t -= 1;
            }
            ans = ans.max(t);
        }
        ans
    }
}
