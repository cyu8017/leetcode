// LeetCode 1276 - Number of Burgers with No Waste of Ingredients
// https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

impl Solution {
    pub fn num_of_burgers(tomato_slices: i32, cheese_slices: i32) -> Vec<i32> {
        if tomato_slices % 2 != 0 {
            return vec![];
        }
        let jumbo = tomato_slices / 2 - cheese_slices;
        let small = cheese_slices - jumbo;
        if jumbo >= 0 && small >= 0 {
            vec![jumbo, small]
        } else {
            vec![]
        }
    }
}
