// LeetCode 0163 - Missing Ranges
impl Solution {
    pub fn find_missing_ranges(nums: Vec<i32>, lower: i32, upper: i32) -> Vec<Vec<i32>> {
        let mut result = Vec::new();
        let mut previous = lower as i64 - 1;
        for current in nums.into_iter().map(|n| n as i64).chain(std::iter::once(upper as i64 + 1)) {
            if current - previous >= 2 { result.push(vec![(previous + 1) as i32, (current - 1) as i32]); }
            previous = current;
        }
        result
    }
}