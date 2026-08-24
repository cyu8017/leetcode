// LeetCode 0667 - Beautiful Arrangement II
// https://leetcode.com/problems/beautiful-arrangement-ii/

impl Solution {
    pub fn construct_array(n: i32, k: i32) -> Vec<i32> {
        let mut res = Vec::new();
        for i in 1..=n - k {
            res.push(i);
        }
        let mut left = n - k + 1;
        let mut right = n;
        let mut take_high = true;
        while left <= right {
            if take_high {
                res.push(right);
                right -= 1;
            } else {
                res.push(left);
                left += 1;
            }
            take_high = !take_high;
        }
        res
    }
}
