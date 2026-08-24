// LeetCode 2570 - Merge Two 2D Arrays by Summing Values
// https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

impl Solution {
    pub fn merge_arrays(nums1: Vec<Vec<i32>>, nums2: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut i = 0;
        let mut j = 0;
        let mut ans = Vec::new();
        while i < nums1.len() && j < nums2.len() {
            if nums1[i][0] == nums2[j][0] {
                ans.push(vec![nums1[i][0], nums1[i][1] + nums2[j][1]]);
                i += 1;
                j += 1;
            } else if nums1[i][0] < nums2[j][0] {
                ans.push(vec![nums1[i][0], nums1[i][1]]);
                i += 1;
            } else {
                ans.push(vec![nums2[j][0], nums2[j][1]]);
                j += 1;
            }
        }
        while i < nums1.len() {
            ans.push(vec![nums1[i][0], nums1[i][1]]);
            i += 1;
        }
        while j < nums2.len() {
            ans.push(vec![nums2[j][0], nums2[j][1]]);
            j += 1;
        }
        ans
    }
}
