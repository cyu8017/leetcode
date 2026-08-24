// LeetCode 2717 - Semi-Ordered Permutation
// https://leetcode.com/problems/semi-ordered-permutation/

impl Solution {
    pub fn semi_ordered_permutation(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut p1 = 0;
        let mut pn = 0;
        for i in 0..n {
            if nums[i] == 1 {
                p1 = i;
            }
            if nums[i] == n as i32 {
                pn = i;
            }
        }
        let mut ans = p1 as i32 + (n as i32 - 1 - pn as i32);
        if p1 > pn {
            ans -= 1;
        }
        ans
    }
}
