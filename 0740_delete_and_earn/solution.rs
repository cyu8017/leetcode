// LeetCode 0740 - Delete and Earn
// https://leetcode.com/problems/delete-and-earn/

impl Solution {
    pub fn delete_and_earn(nums: Vec<i32>) -> i32 {
        if nums.is_empty() {
            return 0;
        }
        let max_num = *nums.iter().max().unwrap() as usize;
        let mut points = vec![0; max_num + 1];
        for num in nums {
            points[num as usize] += num;
        }
        let mut take = 0;
        let mut skip = 0;
        for value in points {
            let new_take = skip + value;
            let new_skip = skip.max(take);
            take = new_take;
            skip = new_skip;
        }
        take.max(skip)
    }
}
