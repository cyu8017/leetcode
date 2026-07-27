// LeetCode 1674 - Minimum Moves to Make Array Complementary
// https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

impl Solution {
    pub fn min_moves(nums: Vec<i32>, limit: i32) -> i32 {
        let n = nums.len();
        let mut d = vec![0i32; (2 * limit + 2) as usize];
        for i in 0..n / 2 {
            let a = nums[i];
            let b = nums[n - 1 - i];
            let lo = a.min(b) + 1;
            let hi = a.max(b) + limit;
            let s = a + b;
            d[2] += 2;
            d[lo as usize] -= 1;
            d[s as usize] -= 1;
            d[(s + 1) as usize] += 1;
            d[(hi + 1) as usize] += 1;
        }
        let mut ans = i32::MAX;
        let mut cur = 0i32;
        for s in 2..=(2 * limit) as usize {
            cur += d[s];
            ans = ans.min(cur);
        }
        ans
    }
}
