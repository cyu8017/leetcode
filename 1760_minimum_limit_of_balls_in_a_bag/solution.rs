// LeetCode 1760 - Minimum Limit of Balls in a Bag
// https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

impl Solution {
    pub fn minimum_size(nums: Vec<i32>, max_operations: i32) -> i32 {
        let mut lo: i32 = 1;
        let mut hi: i32 = *nums.iter().max().unwrap();
        while lo < hi {
            let mid = (lo + hi) / 2;
            let ops: i64 = nums.iter().map(|&x| ((x - 1) / mid) as i64).sum();
            if ops <= max_operations as i64 {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
