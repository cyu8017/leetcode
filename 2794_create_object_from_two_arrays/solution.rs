// LeetCode 2794 - Create Object from Two Arrays
// https://leetcode.com/problems/create-object-from-two-arrays/

use std::collections::HashMap;

impl Solution {
    pub fn create_object(keys_arr: Vec<String>, values_arr: Vec<i32>) -> HashMap<String, i32> {
        let n = keys_arr.len().min(values_arr.len());
        let mut out = HashMap::new();
        for i in 0..n {
            out.entry(keys_arr[i].clone()).or_insert(values_arr[i]);
        }
        out
    }
}
