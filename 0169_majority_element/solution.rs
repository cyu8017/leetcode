// LeetCode 0169 - Majority Element
impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let (mut candidate, mut count) = (0, 0);
        for n in nums {
            if count == 0 { candidate = n; }
            if n == candidate { count += 1; } else { count -= 1; }
        }
        candidate
    }
}