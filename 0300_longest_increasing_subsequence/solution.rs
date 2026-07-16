// LeetCode 0300 - Longest Increasing Subsequence
// https://leetcode.com/problems/longest-increasing-subsequence/

impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let mut piles: Vec<i32> = Vec::new();

        for num in nums {
            let mut left = 0;
            let mut right = piles.len();
            while left < right {
                let mid = left + (right - left) / 2;
                if piles[mid] < num {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            if left == piles.len() {
                piles.push(num);
            } else {
                piles[left] = num;
            }
        }

        piles.len() as i32
    }
}
