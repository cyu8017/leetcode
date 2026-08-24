struct Solution;
// LeetCode 3942 - Minimum Operations To Sort A Permutation
// https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let mut zero = 0;
        for i in 0..n {
            if nums[i as usize] == 0 {
                zero = i;
                break;
            }
        }
        let check = |step: i32| -> bool {
            for i in 1..n {
                let prev = ((zero + (i - 1) * step) % n + n) % n;
                let curr = ((zero + i * step) % n + n) % n;
                if nums[prev as usize] > nums[curr as usize] {
                    return false;
                }
            }
            true
        };
        let mut ans = i32::MAX;
        if check(1) {
            ans = ans.min(zero);
            ans = ans.min(n - zero + 2);
        }
        if check(-1) {
            ans = ans.min(zero + 2);
            ans = ans.min(n - zero);
        }
        if ans == i32::MAX {
            -1
        } else {
            ans
        }
    }
}

fn main() {}
