// LeetCode 3866 - First Unique Even Element
// https://leetcode.com/problems/first-unique-even-element/

impl Solution {
    pub fn first_unique_even(nums: Vec<i32>) -> i32 {
        let mut cnt = [0; 101];
        for &x in &nums {
            cnt[x as usize] += 1;
        }
        for x in nums {
            if x % 2 == 0 && cnt[x as usize] == 1 {
                return x;
            }
        }
        -1
    }
}
