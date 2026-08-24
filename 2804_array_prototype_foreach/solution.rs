// LeetCode 2804 - Array Prototype ForEach
// https://leetcode.com/problems/array-prototype-foreach/

impl Solution {
    pub fn for_each<F: FnMut(i32, i32, &Vec<i32>)>(arr: &Vec<i32>, mut callback: F) {
        for i in 0..arr.len() {
            callback(arr[i], i as i32, arr);
        }
    }
}
