// LeetCode 3555 - Smallest Subarray to Sort in Every Sliding Window
// https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/

impl Solution {
    pub fn min_subarray_sort(nums: Vec<i32>, k: i32) -> Vec<i32> {
        const INF: i32 = 1 << 30;
        let n = nums.len();
        let k = k as usize;
        let f = |i: usize, j: usize| -> i32 {
            let mut mi = INF;
            let mut mx = -INF;
            let mut l = -1i32;
            let mut r = -1i32;
            for p in i..=j {
                if nums[p] < mx {
                    r = p as i32;
                } else {
                    mx = nums[p];
                }
                let q = j - p + i;
                if nums[q] > mi {
                    l = q as i32;
                } else {
                    mi = nums[q];
                }
            }
            if r == -1 {
                0
            } else {
                r - l + 1
            }
        };
        (0..=n - k).map(|i| f(i, i + k - 1)).collect()
    }
}
