// LeetCode 3159 - Find Occurrences of an Element in an Array
// https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/

impl Solution {
    pub fn occurrences_of_element(nums: Vec<i32>, queries: Vec<i32>, x: i32) -> Vec<i32> {
        let ids: Vec<i32> = nums
            .iter()
            .enumerate()
            .filter(|(_, &v)| v == x)
            .map(|(i, _)| i as i32)
            .collect();
        queries
            .into_iter()
            .map(|i| {
                if (i as usize) - 1 < ids.len() {
                    ids[i as usize - 1]
                } else {
                    -1
                }
            })
            .collect()
    }
}
