// LeetCode 0904 - Fruit Into Baskets
// https://leetcode.com/problems/fruit-into-baskets/

use std::collections::HashMap;

impl Solution {
    pub fn total_fruit(fruits: Vec<i32>) -> i32 {
        let mut count = HashMap::new();
        let mut left = 0;
        let mut ans = 0;
        for right in 0..fruits.len() {
            *count.entry(fruits[right]).or_insert(0) += 1;
            while count.len() > 2 {
                let e = count.get_mut(&fruits[left]).unwrap();
                *e -= 1;
                if *e == 0 {
                    count.remove(&fruits[left]);
                }
                left += 1;
            }
            ans = ans.max((right - left + 1) as i32);
        }
        ans
    }
}
