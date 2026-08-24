// LeetCode 0905 - Sort Array By Parity
// https://leetcode.com/problems/sort-array-by-parity/

impl Solution {
    pub fn sort_array_by_parity(mut nums: Vec<i32>) -> Vec<i32> {
        let mut i = 0;
        for j in 0..nums.len() {
            if nums[j] % 2 == 0 {
                nums.swap(i, j);
                i += 1;
            }
        }
        nums
    }
}
