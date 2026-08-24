struct Solution;
// LeetCode 3232 - Find if Digit Game Can Be Won
// https://leetcode.com/problems/find-if-digit-game-can-be-won/

impl Solution {
    pub fn can_alice_win(nums: Vec<i32>) -> bool {
        let mut a = 0;
        let mut b = 0;
        for x in nums {
            if x < 10 {
                a += x;
            } else {
                b += x;
            }
        }
        a != b
    }
}

fn main() {}
