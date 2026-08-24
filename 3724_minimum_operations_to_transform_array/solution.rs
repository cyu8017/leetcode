// LeetCode 3724 - Minimum Operations to Transform Array
// https://leetcode.com/problems/minimum-operations-to-transform-array/

impl Solution {
    pub fn min_operations(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        let mut ans = 1i64;
        let n = nums1.len();
        let mut ok = false;
        let mut d = 1 << 30;
        for i in 0..n {
            let x = nums1[i].max(nums2[i]);
            let y = nums1[i].min(nums2[i]);
            ans += (x - y) as i64;
            d = d.min((x - nums2[n]).abs()).min((y - nums2[n]).abs());
            if nums2[n] >= y && nums2[n] <= x {
                ok = true;
            }
        }
        if !ok {
            ans += d as i64;
        }
        ans
    }
}
