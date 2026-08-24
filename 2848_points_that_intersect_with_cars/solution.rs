// LeetCode 2848 - Points That Intersect With Cars
// https://leetcode.com/problems/points-that-intersect-with-cars/

impl Solution {
    pub fn number_of_points(nums: Vec<Vec<i32>>) -> i32 {
        let mut cov = [0i32; 102];
        for r in nums {
            for x in r[0]..=r[1] {
                cov[x as usize] = 1;
            }
        }
        cov.iter().sum()
    }
}
