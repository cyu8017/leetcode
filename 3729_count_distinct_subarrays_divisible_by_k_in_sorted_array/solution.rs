// LeetCode 3729 - Count Distinct Subarrays Divisible by K in Sorted Array
// https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/

use std::collections::HashMap;

impl Solution {
    pub fn num_good_subarrays(nums: Vec<i32>, k: i32) -> i64 {
        let mut ans = 0i64;
        let mut s = 0;
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        cnt.insert(0, 1);
        for &x in &nums {
            s = (s + x) % k;
            ans += *cnt.get(&s).unwrap_or(&0) as i64;
            *cnt.entry(s).or_insert(0) += 1;
        }
        let n = nums.len();
        let mut i = 0;
        while i < n {
            let mut j = i + 1;
            while j < n && nums[j] == nums[i] {
                j += 1;
            }
            let m = j - i;
            for h in 1..=m {
                if (nums[i] as i64) * (h as i64) % (k as i64) == 0 {
                    ans -= (m - h) as i64;
                }
            }
            i = j;
        }
        ans
    }
}
