// LeetCode 1299 - Replace Elements with Greatest Element on Right Side
// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

impl Solution {
    pub fn replace_elements(mut arr: Vec<i32>) -> Vec<i32> {
        let mut greatest = -1;
        for i in (0..arr.len()).rev() {
            let cur = arr[i];
            arr[i] = greatest;
            greatest = greatest.max(cur);
        }
        arr
    }
}
