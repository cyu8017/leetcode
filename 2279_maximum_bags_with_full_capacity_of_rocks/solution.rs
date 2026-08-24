// LeetCode 2279 - Maximum Bags With Full Capacity of Rocks
// https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

impl Solution {
    pub fn maximum_bags(capacity: Vec<i32>, rocks: Vec<i32>, mut additional_rocks: i32) -> i32 {
        let mut need: Vec<i32> = capacity.iter().zip(rocks.iter()).map(|(c, r)| c - r).collect();
        need.sort_unstable();
        let mut ans = 0;
        for n in need {
            if additional_rocks < n {
                break;
            }
            additional_rocks -= n;
            ans += 1;
        }
        ans
    }
}
