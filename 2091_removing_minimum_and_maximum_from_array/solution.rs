// LeetCode 2091 - Removing Minimum and Maximum From Array
// https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

impl Solution {
    pub fn minimum_deletions(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let mut mi = 0;
        let mut ma = 0;
        for i in 1..nums.len() {
            if nums[i] < nums[mi] {
                mi = i;
            }
            if nums[i] > nums[ma] {
                ma = i;
            }
        }
        let (mi, ma) = if mi > ma { (ma, mi) } else { (mi, ma) };
        let mi = mi as i32;
        let ma = ma as i32;
        (ma + 1).min(n - mi).min(mi + 1 + n - ma)
    }
}
