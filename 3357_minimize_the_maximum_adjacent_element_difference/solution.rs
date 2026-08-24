// LeetCode 3357 - Minimize the Maximum Adjacent Element Difference
// https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/

impl Solution {
    pub fn min_difference(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let ok = |d: i32| -> bool {
            let mut prev = -1;
            let mut i = 0;
            while i < n {
                if nums[i] != -1 {
                    if prev != -1 && (nums[i] - prev).abs() > d {
                        return false;
                    }
                    prev = nums[i];
                    i += 1;
                    continue;
                }
                let mut j = i;
                while j < n && nums[j] == -1 {
                    j += 1;
                }
                let left = prev;
                let right = if j < n { nums[j] } else { -1 };
                let gap = (j - i) as i32;
                if left == -1 && right == -1 {
                    return true;
                }
                if left == -1 || right == -1 {
                    prev = -1;
                    i = j;
                    continue;
                }
                if (left - right).abs() > d * (gap + 1) {
                    return false;
                }
                prev = -1;
                i = j;
            }
            true
        };
        let mut lo = 0;
        let mut hi = 1_000_000_000;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if ok(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
