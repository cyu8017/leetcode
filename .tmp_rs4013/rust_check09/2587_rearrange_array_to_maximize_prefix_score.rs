struct Solution;

// LeetCode 2587 - Rearrange Array to Maximize Prefix Score
// https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/

impl Solution {
    pub fn max_score(mut nums: Vec<i32>) -> i32 {
        nums.sort_by(|a, b| b.cmp(a));
        let mut sum = 0i64;
        let mut ans = 0;
        for x in nums {
            sum += x as i64;
            if sum > 0 {
                ans += 1;
            } else {
                break;
            }
        }
        ans
    }
}

fn main() {}
