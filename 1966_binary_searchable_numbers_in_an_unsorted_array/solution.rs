// LeetCode 1966 - Binary Searchable Numbers in an Unsorted Array
// https://leetcode.com/problems/binary-searchable-numbers-in-an-unsorted-array/

impl Solution {
    pub fn binary_searchable_numbers(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ok = vec![1i32; n];
        let mut mx = i32::MIN;
        for (i, &x) in nums.iter().enumerate() {
            if x < mx {
                ok[i] = 0;
            } else {
                mx = x;
            }
        }
        let mut mi = i32::MAX;
        for i in (0..n).rev() {
            if nums[i] > mi {
                ok[i] = 0;
            } else {
                mi = nums[i];
            }
        }
        ok.into_iter().sum()
    }
}
