// LeetCode 1196 - How Many Apples Can You Put into the Basket
// https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

impl Solution {
    pub fn max_number_of_apples(mut weight: Vec<i32>) -> i32 {
        weight.sort_unstable();
        let mut total = 0;
        for (i, &w) in weight.iter().enumerate() {
            total += w;
            if total > 5000 {
                return i as i32;
            }
        }
        weight.len() as i32
    }
}
