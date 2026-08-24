// LeetCode 3737 - Count Subarrays With Majority Element I
// https://leetcode.com/problems/count-subarrays-with-majority-element-i/

impl Solution {
    pub fn count_majority_subarrays(nums: Vec<i32>, target: i32) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for i in 0..n {
            let mut cnt = 0;
            for j in i..n {
                if nums[j] == target {
                    cnt += 1;
                }
                if cnt * 2 > (j - i + 1) as i32 {
                    ans += 1;
                }
            }
        }
        ans
    }
}
