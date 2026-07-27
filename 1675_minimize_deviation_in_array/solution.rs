// LeetCode 1675 - Minimize Deviation in Array
// https://leetcode.com/problems/minimize-deviation-in-array/

use std::collections::BinaryHeap;

impl Solution {
    pub fn minimum_deviation(nums: Vec<i32>) -> i32 {
        let mut heap = BinaryHeap::new();
        let mut mn = i32::MAX;
        for mut x in nums {
            if x % 2 == 1 {
                x *= 2;
            }
            mn = mn.min(x);
            heap.push(x);
        }
        let mut ans = i32::MAX;
        loop {
            let x = heap.pop().unwrap();
            ans = ans.min(x - mn);
            if x % 2 == 1 {
                return ans;
            }
            let nx = x / 2;
            mn = mn.min(nx);
            heap.push(nx);
        }
    }
}
