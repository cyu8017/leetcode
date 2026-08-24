// LeetCode 3638 - Maximum Balanced Shipments
// https://leetcode.com/problems/maximum-balanced-shipments/

impl Solution {
    pub fn max_balanced_shipments(weight: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut mx = 0;
        for x in weight {
            mx = mx.max(x);
            if x < mx {
                ans += 1;
                mx = 0;
            }
        }
        ans
    }
}
