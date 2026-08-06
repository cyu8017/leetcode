// LeetCode 1122 - Relative Sort Array
// https://leetcode.com/problems/relative-sort-array/

use std::collections::HashMap;

impl Solution {
    pub fn relative_sort_array(arr1: Vec<i32>, arr2: Vec<i32>) -> Vec<i32> {
        let mut count: HashMap<i32, i32> = HashMap::new();
        for x in &arr1 {
            *count.entry(*x).or_insert(0) += 1;
        }
        let mut ans = Vec::with_capacity(arr1.len());
        for x in arr2 {
            if let Some(c) = count.get_mut(&x) {
                for _ in 0..*c {
                    ans.push(x);
                }
                count.remove(&x);
            }
        }
        let mut rest: Vec<i32> = count.keys().copied().collect();
        rest.sort_unstable();
        for x in rest {
            for _ in 0..count[&x] {
                ans.push(x);
            }
        }
        ans
    }
}
