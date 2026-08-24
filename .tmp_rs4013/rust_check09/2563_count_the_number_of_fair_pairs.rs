struct Solution;

// LeetCode 2563 - Count the Number of Fair Pairs
// https://leetcode.com/problems/count-the-number-of-fair-pairs/

impl Solution {
    pub fn count_fair_pairs(mut nums: Vec<i32>, lower: i32, upper: i32) -> i64 {
        nums.sort_unstable();
        let count = |x: i32| {
            let mut ans = 0i64;
            let mut l = 0;
            let mut r = nums.len() as i32 - 1;
            while l < r {
                if nums[l as usize] + nums[r as usize] <= x {
                    ans += (r - l) as i64;
                    l += 1;
                } else {
                    r -= 1;
                }
            }
            ans
        };
        count(upper) - count(lower - 1)
    }
}

fn main() {}
