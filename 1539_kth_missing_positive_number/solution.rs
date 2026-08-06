// LeetCode 1539 - Kth Missing Positive Number
// https://leetcode.com/problems/kth-missing-positive-number/

impl Solution {
    pub fn find_kth_positive(arr: Vec<i32>, k: i32) -> i32 {
        let mut left = 0;
        let mut right = arr.len();
        while left < right {
            let middle = (left + right) / 2;
            if arr[middle] - middle as i32 - 1 < k {
                left = middle + 1;
            } else {
                right = middle;
            }
        }
        left as i32 + k
    }
}
