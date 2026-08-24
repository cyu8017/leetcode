// LeetCode 3510 - Minimum Pair Removal to Sort Array II
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

use std::collections::BTreeSet;

impl Solution {
    pub fn minimum_pair_removal(mut nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut inv = 0i32;
        let mut ans = 0i32;
        let mut sl: BTreeSet<(i64, usize)> = BTreeSet::new();
        let mut idx: BTreeSet<usize> = (0..n).collect();
        for i in 0..n - 1 {
            if nums[i] > nums[i + 1] {
                inv += 1;
            }
            sl.insert((nums[i] as i64 + nums[i + 1] as i64, i));
        }
        while inv > 0 {
            ans += 1;
            let (s, i) = sl.iter().next().copied().unwrap();
            sl.remove(&(s, i));
            let j = *idx.range((i + 1)..).next().unwrap();
            if nums[i] > nums[j] {
                inv -= 1;
            }
            if let Some(&h) = idx.range(..i).next_back() {
                if nums[h] > nums[i] {
                    inv -= 1;
                }
                sl.remove(&(nums[h] as i64 + nums[i] as i64, h));
                if nums[h] as i64 > s {
                    inv += 1;
                }
                sl.insert((nums[h] as i64 + s, h));
            }
            if let Some(&k) = idx.range((j + 1)..).next() {
                if nums[j] > nums[k] {
                    inv -= 1;
                }
                sl.remove(&(nums[j] as i64 + nums[k] as i64, j));
                if s > nums[k] as i64 {
                    inv += 1;
                }
                sl.insert((s + nums[k] as i64, i));
            }
            nums[i] = s as i32;
            idx.remove(&j);
        }
        ans
    }
}
