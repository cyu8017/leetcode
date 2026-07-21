// LeetCode 1846 - Maximum Element After Decreasing and Rearranging
// https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

impl Solution {
    pub fn maximum_element_after_decrementing_and_rearranging(mut arr: Vec<i32>) -> i32 {
        arr.sort_unstable();
        arr[0] = 1;
        for i in 1..arr.len() {
            arr[i] = arr[i].min(arr[i - 1] + 1);
        }
        *arr.iter().max().unwrap()
    }
}
