// LeetCode 2098 - Subsequence of Size K With the Largest Even Sum
// https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/

impl Solution {
    pub fn largest_even_sum(mut nums: Vec<i32>, k: i32) -> i64 {
        nums.sort_unstable_by(|a, b| b.cmp(a));
        let k = k as usize;
        let mut sum: i64 = nums[..k].iter().map(|&x| x as i64).sum();
        if sum % 2 == 0 {
            return sum;
        }
        let mut ans = -1i64;
        let mut odd_in = None;
        let mut even_in = None;
        let mut odd_out = None;
        let mut even_out = None;
        for i in (0..k).rev() {
            if nums[i] % 2 != 0 && odd_in.is_none() {
                odd_in = Some(i);
            }
            if nums[i] % 2 == 0 && even_in.is_none() {
                even_in = Some(i);
            }
        }
        for i in k..nums.len() {
            if nums[i] % 2 != 0 && odd_out.is_none() {
                odd_out = Some(i);
            }
            if nums[i] % 2 == 0 && even_out.is_none() {
                even_out = Some(i);
            }
        }
        if let (Some(oi), Some(eo)) = (odd_in, even_out) {
            ans = ans.max(sum - nums[oi] as i64 + nums[eo] as i64);
        }
        if let (Some(ei), Some(oo)) = (even_in, odd_out) {
            ans = ans.max(sum - nums[ei] as i64 + nums[oo] as i64);
        }
        ans
    }
}
