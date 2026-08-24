// LeetCode 2600 - K Items With the Maximum Sum
// https://leetcode.com/problems/k-items-with-the-maximum-sum/

impl Solution {
    pub fn k_items_with_maximum_sum(num_ones: i32, num_zeros: i32, num_neg_ones: i32, mut k: i32) -> i32 {
        let mut ans = 0;
        let take = num_ones.min(k);
        ans += take;
        k -= take;
        let take = num_zeros.min(k);
        k -= take;
        let take = num_neg_ones.min(k);
        ans -= take;
        ans
    }
}
