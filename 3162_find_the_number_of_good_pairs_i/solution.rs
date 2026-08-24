// LeetCode 3162 - Find the Number of Good Pairs I
// https://leetcode.com/problems/find-the-number-of-good-pairs-i/

impl Solution {
    pub fn number_of_pairs(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i32 {
        let mut ans = 0;
        for &x in &nums1 {
            for &y in &nums2 {
                if x % (y * k) == 0 {
                    ans += 1;
                }
            }
        }
        ans
    }
}
