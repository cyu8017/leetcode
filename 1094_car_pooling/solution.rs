// LeetCode 1094 - Car Pooling
// https://leetcode.com/problems/car-pooling/

impl Solution {
    pub fn car_pooling(trips: Vec<Vec<i32>>, capacity: i32) -> bool {
        let mut diff = [0i32; 1001];
        for trip in &trips {
            diff[trip[1] as usize] += trip[0];
            diff[trip[2] as usize] -= trip[0];
        }
        let mut cur = 0;
        for &x in &diff {
            cur += x;
            if cur > capacity {
                return false;
            }
        }
        true
    }
}
