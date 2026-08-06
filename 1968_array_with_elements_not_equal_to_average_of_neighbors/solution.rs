// LeetCode 1968 - Array With Elements Not Equal to Average of Neighbors
// https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

impl Solution {
    pub fn rearrange_array(mut nums: Vec<i32>) -> Vec<i32> {
        nums.sort_unstable();
        let n = nums.len();
        let mid = (n + 1) / 2;
        let small = &nums[..mid];
        let large = &nums[mid..];
        let mut ans = Vec::with_capacity(n);
        let mut i = 0;
        let mut j = 0;
        while i < small.len() || j < large.len() {
            if i < small.len() {
                ans.push(small[i]);
                i += 1;
            }
            if j < large.len() {
                ans.push(large[j]);
                j += 1;
            }
        }
        ans
    }
}
