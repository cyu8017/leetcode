// LeetCode 1855 - Maximum Distance Between a Pair of Values
// https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

impl Solution {
    pub fn max_distance(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut answer = 0i32;
        let mut j = 0usize;
        for (i, &value) in nums1.iter().enumerate() {
            while j < nums2.len() && value <= nums2[j] {
                j += 1;
            }
            answer = answer.max(j as i32 - i as i32 - 1);
        }
        answer
    }
}
