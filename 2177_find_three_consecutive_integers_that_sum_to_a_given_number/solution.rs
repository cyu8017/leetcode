// LeetCode 2177 - Find Three Consecutive Integers That Sum to a Given Number
// https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

impl Solution {
    pub fn sum_of_three(num: i64) -> Vec<i64> {
        if num % 3 != 0 {
            return vec![];
        }
        let x = num / 3;
        vec![x - 1, x, x + 1]
    }
}
