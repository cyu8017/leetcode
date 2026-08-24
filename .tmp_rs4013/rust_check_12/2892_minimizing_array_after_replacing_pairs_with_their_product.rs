struct Solution;
// LeetCode 2892 - Minimizing Array After Replacing Pairs With Their Product
// https://leetcode.com/problems/minimizing-array-after-replacing-pairs-with-their-product/

impl Solution {
    pub fn min_array_length(nums: Vec<i32>, k: i32) -> i32 {
        if nums.is_empty() {
            return 0;
        }
        let mut ans = 1;
        let mut prod = nums[0] as i64;
        let k = k as i64;
        for &v in nums.iter().skip(1) {
            let v = v as i64;
            if prod <= k && v <= k && (v == 0 || prod <= k / v) {
                prod *= v;
            } else {
                ans += 1;
                prod = v;
            }
        }
        ans
    }
}

fn main() {}
