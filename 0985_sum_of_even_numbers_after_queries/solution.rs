// LeetCode 0985 - Sum of Even Numbers After Queries
// https://leetcode.com/problems/sum-of-even-numbers-after-queries/

impl Solution {
    pub fn sum_even_after_queries(mut nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut even = nums.iter().filter(|&&x| x % 2 == 0).sum::<i32>();
        let mut ans = Vec::with_capacity(queries.len());
        for q in queries {
            let val = q[0];
            let i = q[1] as usize;
            if nums[i] % 2 == 0 {
                even -= nums[i];
            }
            nums[i] += val;
            if nums[i] % 2 == 0 {
                even += nums[i];
            }
            ans.push(even);
        }
        ans
    }
}
