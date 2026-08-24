// LeetCode 2210 - Count Hills and Valleys in an Array
// https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

impl Solution {
    pub fn count_hill_valley(nums: Vec<i32>) -> i32 {
        let mut compact = vec![nums[0]];
        for &x in nums.iter().skip(1) {
            if x != *compact.last().unwrap() {
                compact.push(x);
            }
        }
        let mut ans = 0;
        for i in 1..compact.len().saturating_sub(1) {
            if (compact[i] > compact[i - 1] && compact[i] > compact[i + 1])
                || (compact[i] < compact[i - 1] && compact[i] < compact[i + 1])
            {
                ans += 1;
            }
        }
        ans
    }
}
