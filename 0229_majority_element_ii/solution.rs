// LeetCode 0229 - Majority Element II
// https://leetcode.com/problems/majority-element-ii/

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> Vec<i32> {
        let mut candidate1: Option<i32> = None;
        let mut candidate2: Option<i32> = None;
        let mut count1 = 0;
        let mut count2 = 0;

        for num in nums.iter().copied() {
            if Some(num) == candidate1 {
                count1 += 1;
            } else if Some(num) == candidate2 {
                count2 += 1;
            } else if count1 == 0 {
                candidate1 = Some(num);
                count1 = 1;
            } else if count2 == 0 {
                candidate2 = Some(num);
                count2 = 1;
            } else {
                count1 -= 1;
                count2 -= 1;
            }
        }

        count1 = 0;
        count2 = 0;
        for num in nums.iter().copied() {
            if Some(num) == candidate1 {
                count1 += 1;
            } else if Some(num) == candidate2 {
                count2 += 1;
            }
        }

        let threshold = (nums.len() / 3) as i32;
        let mut result = Vec::new();
        if count1 > threshold {
            result.push(candidate1.unwrap());
        }
        if candidate2.is_some()
            && candidate2 != candidate1
            && count2 > threshold
        {
            result.push(candidate2.unwrap());
        }
        result
    }
}
