// LeetCode 3397 - Maximum Number of Distinct Elements After Operations
// https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

impl Solution {
    pub fn max_distinct_elements(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort_unstable();
        let mut ans = 0;
        let mut prev = i64::MIN / 2;
        for x in nums {
            let mut cur = x as i64 - k as i64;
            if cur <= prev {
                cur = prev + 1;
            }
            if cur > x as i64 + k as i64 {
                continue;
            }
            ans += 1;
            prev = cur;
        }
        ans
    }
}
