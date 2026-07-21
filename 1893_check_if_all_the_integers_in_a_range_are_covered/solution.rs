// LeetCode 1893 - Check if All the Integers in a Range Are Covered
// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

impl Solution {
    pub fn is_covered(ranges: Vec<Vec<i32>>, left: i32, right: i32) -> bool {
        let mut covered = [false; 51];
        for r in &ranges {
            for value in r[0]..=r[1] {
                covered[value as usize] = true;
            }
        }
        (left..=right).all(|value| covered[value as usize])
    }
}
