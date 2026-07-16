// LeetCode 0215 - Kth Largest Element in an Array
// https://leetcode.com/problems/kth-largest-element-in-an-array/

impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        let mut nums = nums;
        let target = nums.len() - k as usize;
        let mut left = 0usize;
        let mut right = nums.len() - 1;
        while left <= right {
            let pivot_index = partition(&mut nums, left, right);
            match pivot_index.cmp(&target) {
                std::cmp::Ordering::Equal => return nums[pivot_index],
                std::cmp::Ordering::Less => left = pivot_index + 1,
                std::cmp::Ordering::Greater => right = pivot_index - 1,
            }
        }
        nums[left]
    }
}

fn partition(nums: &mut [i32], left: usize, right: usize) -> usize {
    let pivot_index = left + (right - left) / 2;
    nums.swap(pivot_index, right);
    let mut store = left;
    for i in left..right {
        if nums[i] <= nums[right] {
            nums.swap(store, i);
            store += 1;
        }
    }
    nums.swap(store, right);
    store
}
