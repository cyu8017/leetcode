struct Solution;
// LeetCode 3940 - Limit Occurrences In Sorted Array
// https://leetcode.com/problems/limit-occurrences-in-sorted-array/

impl Solution {
    pub fn limit_occurrences(mut nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        if n == 0 {
            return nums;
        }
        let mut cnt = 1;
        let mut l = 1;
        for r in 1..n {
            if nums[r] != nums[r - 1] {
                cnt = 1;
            } else {
                cnt += 1;
            }
            if cnt <= k {
                nums[l] = nums[r];
                l += 1;
            }
        }
        nums.truncate(l);
        nums
    }
}

fn main() {}
