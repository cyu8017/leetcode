// LeetCode 2782 - Number of Unique Categories
// https://leetcode.com/problems/number-of-unique-categories/

use std::collections::HashSet;

impl Solution {
    pub fn number_of_categories(_n: i32, category_handler: Vec<i32>) -> i32 {
        category_handler.into_iter().collect::<HashSet<_>>().len() as i32
    }
}
