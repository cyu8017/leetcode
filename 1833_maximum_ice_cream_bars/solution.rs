// LeetCode 1833 - Maximum Ice Cream Bars
// https://leetcode.com/problems/maximum-ice-cream-bars/

impl Solution {
    pub fn max_ice_cream(mut costs: Vec<i32>, mut coins: i32) -> i32 {
        costs.sort_unstable();
        let mut count = 0;
        for cost in costs {
            if coins < cost {
                break;
            }
            coins -= cost;
            count += 1;
        }
        count
    }
}
