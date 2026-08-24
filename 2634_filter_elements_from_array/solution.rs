// LeetCode 2634 - Filter Elements from Array
// https://leetcode.com/problems/filter-elements-from-array/

impl Solution {
    pub fn filter(arr: Vec<i32>, f: impl Fn(i32, i32) -> bool) -> Vec<i32> {
        let mut out = Vec::new();
        for (i, x) in arr.into_iter().enumerate() {
            if f(x, i as i32) {
                out.push(x);
            }
        }
        out
    }
}
