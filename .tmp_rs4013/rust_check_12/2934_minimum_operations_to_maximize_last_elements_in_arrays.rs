struct Solution;
// LeetCode 2934 - Minimum Operations to Maximize Last Elements in Arrays
// https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/

impl Solution {
    pub fn min_operations(mut nums1: Vec<i32>, mut nums2: Vec<i32>) -> i32 {
        let n = nums1.len();
        let calc = |a1: &[i32], a2: &[i32]| -> i32 {
            let mut ops = 0;
            let last1 = a1[n - 1];
            let last2 = a2[n - 1];
            for i in 0..n - 1 {
                let x = a1[i];
                let y = a2[i];
                if x <= last1 && y <= last2 {
                    continue;
                }
                if y <= last1 && x <= last2 {
                    ops += 1;
                    continue;
                }
                return 1 << 30;
            }
            ops
        };
        let mut ans = calc(&nums1, &nums2);
        nums1.swap(n - 1, n - 1);
        let tmp = nums1[n - 1];
        nums1[n - 1] = nums2[n - 1];
        nums2[n - 1] = tmp;
        let cand = calc(&nums1, &nums2) + 1;
        if cand < ans {
            ans = cand;
        }
        if ans >= (1 << 30) { -1 } else { ans }
    }
}

fn main() {}
