// LeetCode 1985 - Find the Kth Largest Integer in the Array
// https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

impl Solution {
    pub fn kth_largest_number(mut nums: Vec<String>, k: i32) -> String {
        nums.sort_by(|a, b| b.len().cmp(&a.len()).then(b.cmp(a)));
        nums[(k - 1) as usize].clone()
    }
}
