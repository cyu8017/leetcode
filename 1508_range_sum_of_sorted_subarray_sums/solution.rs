// LeetCode 1508 - Range Sum of Sorted Subarray Sums
// https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

impl Solution {
    pub fn range_sum(nums: Vec<i32>, n: i32, left: i32, right: i32) -> i32 {
        let n = n as usize;
        let mut values = Vec::new();
        for i in 0..n {
            let mut total = 0;
            for j in i..n {
                total += nums[j];
                values.push(total);
            }
        }
        values.sort_unstable();
        let mut ans = 0i64;
        for i in (left as usize - 1)..(right as usize) {
            ans = (ans + values[i] as i64) % 1_000_000_007;
        }
        ans as i32
    }
}
