// LeetCode 2176 - Count Equal and Divisible Pairs in an Array
// https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

impl Solution {
    pub fn count_pairs(nums: Vec<i32>, k: i32) -> i32 {
        let mut ans = 0;
        for i in 0..nums.len() {
            for j in i + 1..nums.len() {
                if nums[i] == nums[j] && (i * j) % (k as usize) == 0 {
                    ans += 1;
                }
            }
        }
        ans
    }
}
