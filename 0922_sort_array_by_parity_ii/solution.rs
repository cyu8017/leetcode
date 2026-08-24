// LeetCode 0922 - Sort Array By Parity II
// https://leetcode.com/problems/sort-array-by-parity-ii/

impl Solution {
    pub fn sort_array_by_parity_ii(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut ans = vec![0; n];
        let mut even = 0;
        let mut odd = 1;
        for x in nums {
            if x % 2 == 0 {
                ans[even] = x;
                even += 2;
            } else {
                ans[odd] = x;
                odd += 2;
            }
        }
        ans
    }
}
