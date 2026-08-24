// LeetCode 3637 - Trionic Array I
// https://leetcode.com/problems/trionic-array-i/

impl Solution {
    pub fn is_trionic(nums: Vec<i32>) -> bool {
        let n = nums.len();
        let mut p = 0;
        while p < n - 2 && nums[p] < nums[p + 1] {
            p += 1;
        }
        if p == 0 {
            return false;
        }
        let mut q = p;
        while q < n - 1 && nums[q] > nums[q + 1] {
            q += 1;
        }
        if q == p || q == n - 1 {
            return false;
        }
        while q < n - 1 && nums[q] < nums[q + 1] {
            q += 1;
        }
        q == n - 1
    }
}
