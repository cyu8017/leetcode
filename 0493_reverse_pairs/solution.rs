// LeetCode 0493 - Reverse Pairs
// https://leetcode.com/problems/reverse-pairs/

impl Solution {
    pub fn reverse_pairs(nums: &mut Vec<i32>) -> i32 {
        Self::merge_sort(nums, 0, nums.len().saturating_sub(1)) as i32
    }

    fn merge_sort(nums: &mut [i32], start: usize, end: usize) -> i64 {
        if start >= end {
            return 0;
        }
        let mid = start + (end - start) / 2;
        let mut count = Self::merge_sort(nums, start, mid) + Self::merge_sort(nums, mid + 1, end);
        let mut j = mid + 1;
        for i in start..=mid {
            while j <= end && nums[i] as i64 > 2 * nums[j] as i64 {
                j += 1;
            }
            count += (j - (mid + 1)) as i64;
        }
        let mut merged = nums[start..=end].to_vec();
        merged.sort_unstable();
        nums[start..=end].copy_from_slice(&merged);
        count
    }
}
