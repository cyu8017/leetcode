// LeetCode 2418 - Sort the People
// https://leetcode.com/problems/sort-the-people/

impl Solution {
    pub fn sort_people(names: Vec<String>, heights: Vec<i32>) -> Vec<String> {
        let n = names.len();
        let mut idx: Vec<usize> = (0..n).collect();
        idx.sort_by(|&a, &b| heights[b].cmp(&heights[a]));
        idx.into_iter().map(|i| names[i].clone()).collect()
    }
}
