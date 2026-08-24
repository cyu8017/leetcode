struct Solution;
// LeetCode 2874 - Maximum Value of an Ordered Triplet II
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

impl Solution {
    pub fn maximum_triplet_value(nums: Vec<i32>) -> i64 {
        let mut ans = 0i64;
        let mut max_i = 0i64;
        let mut max_diff = 0i64;
        for v in nums {
            let val = v as i64;
            if max_diff * val > ans {
                ans = max_diff * val;
            }
            if max_i - val > max_diff {
                max_diff = max_i - val;
            }
            if val > max_i {
                max_i = val;
            }
        }
        ans
    }
}

fn main() {}
