// LeetCode 0031 - Next Permutation
// https://leetcode.com/problems/next-permutation/

impl Solution {
    pub fn next_permutation(&mut self, nums: &mut Vec<i32>) {
        let n = nums.len();
        if n <= 1 {
            return;
        }

        let mut i = n as isize - 2;
        while i >= 0 && nums[i as usize] >= nums[i as usize + 1] {
            i -= 1;
        }

        if i >= 0 {
            let mut j = n - 1;
            while nums[j] <= nums[i as usize] {
                j -= 1;
            }
            nums.swap(i as usize, j);
        }

        let mut left = (i + 1) as usize;
        let mut right = n - 1;
        while left < right {
            nums.swap(left, right);
            left += 1;
            right -= 1;
        }
    }
}
