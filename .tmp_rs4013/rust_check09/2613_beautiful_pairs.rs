struct Solution;

// LeetCode 2613 - Beautiful Pairs
// https://leetcode.com/problems/beautiful-pairs/

impl Solution {
    pub fn beautiful_pair(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let n = nums1.len();
        let mut best_dist = i64::MAX;
        let mut ans = vec![0, 1];
        for i in 0..n {
            for j in i + 1..n {
                let d = (nums1[i] - nums1[j]).abs() as i64 + (nums2[i] - nums2[j]).abs() as i64;
                if d < best_dist
                    || (d == best_dist && (i < ans[0] as usize || (i == ans[0] as usize && j < ans[1] as usize)))
                {
                    best_dist = d;
                    ans = vec![i as i32, j as i32];
                }
            }
        }
        ans
    }
}

fn main() {}
