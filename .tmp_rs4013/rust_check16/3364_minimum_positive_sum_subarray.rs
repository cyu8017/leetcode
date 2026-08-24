struct Solution;
// LeetCode 3364 - Minimum Positive Sum Subarray
// https://leetcode.com/problems/minimum-positive-sum-subarray/

impl Solution {
    pub fn minimum_sum_subarray(nums: Vec<i32>, l: i32, r: i32) -> i32 {
        let n = nums.len();
        let mut pref = vec![0; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + nums[i];
        }
        let mut ans = i32::MAX;
        let mut found = false;
        for i in 0..n {
            let mut length = l;
            while length <= r && i + length as usize <= n {
                let s = pref[i + length as usize] - pref[i];
                if s > 0 && s < ans {
                    ans = s;
                    found = true;
                }
                length += 1;
            }
        }
        if found { ans } else { -1 }
    }
}

fn main() {}
