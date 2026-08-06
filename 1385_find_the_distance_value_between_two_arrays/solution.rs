// LeetCode 1385 - Find the Distance Value Between Two Arrays
// https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

impl Solution {
    pub fn find_the_distance_value(arr1: Vec<i32>, mut arr2: Vec<i32>, d: i32) -> i32 {
        arr2.sort_unstable();
        let mut ans = 0;
        for x in arr1 {
            let i = arr2.partition_point(|&v| v < x);
            let bad = (i < arr2.len() && (arr2[i] - x).abs() <= d)
                || (i > 0 && (arr2[i - 1] - x).abs() <= d);
            if !bad {
                ans += 1;
            }
        }
        ans
    }
}
