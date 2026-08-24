struct Solution;
// LeetCode 3231 - Minimum Number of Increasing Subsequence to Be Removed
// https://leetcode.com/problems/minimum-number-of-increasing-subsequence-to-be-removed/

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut g = Vec::new();
        for x in nums {
            let mut l = 0;
            let mut r = g.len();
            while l < r {
                let mid = (l + r) >> 1;
                if g[mid] < x {
                    r = mid;
                } else {
                    l = mid + 1;
                }
            }
            if l == g.len() {
                g.push(x);
            } else {
                g[l] = x;
            }
        }
        g.len() as i32
    }
}

fn main() {}
