// LeetCode 1387 - Sort Integers by The Power Value
// https://leetcode.com/problems/sort-integers-by-the-power-value/

use std::collections::HashMap;

impl Solution {
    pub fn get_kth(lo: i32, hi: i32, k: i32) -> i32 {
        fn power(x: i32, memo: &mut HashMap<i32, i32>) -> i32 {
            if x == 1 {
                return 0;
            }
            if let Some(&v) = memo.get(&x) {
                return v;
            }
            let v = 1 + if x % 2 == 0 {
                power(x / 2, memo)
            } else {
                power(3 * x + 1, memo)
            };
            memo.insert(x, v);
            v
        }
        let mut memo = HashMap::new();
        let mut nums: Vec<i32> = (lo..=hi).collect();
        nums.sort_by_key(|&x| (power(x, &mut memo), x));
        nums[(k - 1) as usize]
    }
}
