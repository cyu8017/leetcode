// LeetCode 1664 - Ways to Make a Fair Array
// https://leetcode.com/problems/ways-to-make-a-fair-array/

impl Solution {
    pub fn ways_to_make_fair(nums: Vec<i32>) -> i32 {
        let mut te: i32 = nums.iter().step_by(2).sum();
        let mut to: i32 = nums.iter().skip(1).step_by(2).sum();
        let mut le = 0i32;
        let mut lo = 0i32;
        let mut ans = 0i32;
        for (i, &x) in nums.iter().enumerate() {
            if i % 2 == 1 {
                to -= x;
            } else {
                te -= x;
            }
            if le + to == lo + te {
                ans += 1;
            }
            if i % 2 == 1 {
                lo += x;
            } else {
                le += x;
            }
        }
        ans
    }
}
