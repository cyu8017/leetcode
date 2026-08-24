struct Solution;
// LeetCode 3431 - Minimum Unlocked Indices to Sort Nums
// https://leetcode.com/problems/minimum-unlocked-indices-to-sort-nums/

impl Solution {
    pub fn min_unlocked_indices(nums: Vec<i32>, locked: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut need = false;
        for i in 1..n {
            if nums[i] < nums[i - 1] {
                need = true;
                break;
            }
        }
        if !need {
            return 0;
        }
        let mut left = n as i32;
        let mut right = -1;
        for i in 0..n {
            for j in (i + 1)..n {
                if nums[i] > nums[j] {
                    if (i as i32) < left {
                        left = i as i32;
                    }
                    if (j as i32) > right {
                        right = j as i32;
                    }
                }
            }
        }
        if right < left {
            return 0;
        }
        let mut ans = 0;
        for i in left..=right {
            if locked[i as usize] == 1 {
                ans += 1;
            }
        }
        let mut tmp = nums;
        let mut lock = locked;
        for i in left..=right {
            lock[i as usize] = 0;
        }
        let mut changed = true;
        while changed {
            changed = false;
            for i in 0..n - 1 {
                if lock[i] == 0 && lock[i + 1] == 0 && tmp[i] > tmp[i + 1] {
                    tmp.swap(i, i + 1);
                    changed = true;
                }
            }
        }
        for i in 1..n {
            if tmp[i] < tmp[i - 1] {
                return -1;
            }
        }
        ans
    }
}

fn main() {}
