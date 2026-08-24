// LeetCode 3769 - Sort Integers By Binary Reflection
// https://leetcode.com/problems/sort-integers-by-binary-reflection/

impl Solution {
    pub fn sort_by_reflection(mut nums: Vec<i32>) -> Vec<i32> {
        let f = |mut x: i32| {
            let mut y = 0;
            while x != 0 {
                y = (y << 1) | (x & 1);
                x >>= 1;
            }
            y
        };
        nums.sort_by(|&a, &b| {
            let fa = f(a);
            let fb = f(b);
            if fa != fb {
                fa.cmp(&fb)
            } else {
                a.cmp(&b)
            }
        });
        nums
    }
}
