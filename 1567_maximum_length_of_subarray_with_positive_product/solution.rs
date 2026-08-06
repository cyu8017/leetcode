// LeetCode 1567 - Maximum Length of Subarray With Positive Product
// https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

impl Solution {
    pub fn get_max_len(nums: Vec<i32>) -> i32 {
        let mut positive = 0;
        let mut negative = 0;
        let mut answer = 0;
        for x in nums {
            if x == 0 {
                positive = 0;
                negative = 0;
            } else if x > 0 {
                positive += 1;
                negative = if negative > 0 { negative + 1 } else { 0 };
            } else {
                let new_positive = if negative > 0 { negative + 1 } else { 0 };
                negative = positive + 1;
                positive = new_positive;
            }
            answer = answer.max(positive);
        }
        answer
    }
}
