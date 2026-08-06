// LeetCode 1287 - Element Appearing More Than 25% In Sorted Array
// https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

impl Solution {
    pub fn find_special_integer(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        for &value in &[arr[n / 4], arr[n / 2], arr[3 * n / 4]] {
            if arr.iter().filter(|&&x| x == value).count() > n / 4 {
                return value;
            }
        }
        arr[0]
    }
}
