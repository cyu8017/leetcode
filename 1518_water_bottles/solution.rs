// LeetCode 1518 - Water Bottles
// https://leetcode.com/problems/water-bottles/

impl Solution {
    pub fn num_water_bottles(mut num_bottles: i32, num_exchange: i32) -> i32 {
        let mut total = num_bottles;
        while num_bottles >= num_exchange {
            let new_bottles = num_bottles / num_exchange;
            let remainder = num_bottles % num_exchange;
            total += new_bottles;
            num_bottles = new_bottles + remainder;
        }
        total
    }
}
