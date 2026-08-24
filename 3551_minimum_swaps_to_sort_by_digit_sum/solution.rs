// LeetCode 3551 - Minimum Swaps to Sort by Digit Sum
// https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/

use std::collections::HashMap;

impl Solution {
    fn f(mut x: i32) -> i32 {
        let mut s = 0;
        while x > 0 {
            s += x % 10;
            x /= 10;
        }
        s
    }

    pub fn min_swaps(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut arr: Vec<(i32, i32)> = nums.iter().map(|&x| (Self::f(x), x)).collect();
        arr.sort();
        let mut d = HashMap::new();
        for i in 0..n {
            d.insert(arr[i].1, i);
        }
        let mut vis = vec![false; n];
        let mut ans = n as i32;
        for i in 0..n {
            if !vis[i] {
                ans -= 1;
                let mut j = i;
                while !vis[j] {
                    vis[j] = true;
                    j = d[&nums[j]];
                }
            }
        }
        ans
    }
}
