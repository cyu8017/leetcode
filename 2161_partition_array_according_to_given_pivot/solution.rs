// LeetCode 2161 - Partition Array According to Given Pivot
// https://leetcode.com/problems/partition-array-according-to-given-pivot/

impl Solution {
    pub fn pivot_array(nums: Vec<i32>, pivot: i32) -> Vec<i32> {
        let mut less = Vec::new();
        let mut eq = Vec::new();
        let mut greater = Vec::new();
        for x in nums {
            if x < pivot {
                less.push(x);
            } else if x == pivot {
                eq.push(x);
            } else {
                greater.push(x);
            }
        }
        less.extend(eq);
        less.extend(greater);
        less
    }
}
