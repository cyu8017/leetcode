// LeetCode 1431 - Kids With the Greatest Number of Candies
// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

impl Solution {
    pub fn kids_with_candies(candies: Vec<i32>, extra_candies: i32) -> Vec<bool> {
        let maximum = *candies.iter().max().unwrap();
        candies.into_iter().map(|v| v + extra_candies >= maximum).collect()
    }
}
