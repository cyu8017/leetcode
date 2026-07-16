// LeetCode 0315 - Count of Smaller Numbers After Self
// https://leetcode.com/problems/count-of-smaller-numbers-after-self/

impl Solution {
    pub fn count_smaller(nums: Vec<i32>) -> Vec<i32> {
        let mut sorted_nums: Vec<i32> = Vec::new();
        let mut result = vec![0; nums.len()];

        for (index, &num) in nums.iter().enumerate().rev() {
            let position = sorted_nums.partition_point(|&value| value < num);
            result[index] = position as i32;
            sorted_nums.insert(position, num);
        }

        result
    }
}
