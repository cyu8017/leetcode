// LeetCode 0274 - H-Index
// https://leetcode.com/problems/h-index/

impl Solution {
    pub fn h_index(citations: Vec<i32>) -> i32 {
        let mut buckets = vec![0; citations.len() + 1];
        for citation in citations {
            let index = std::cmp::min(citation as usize, citations.len());
            buckets[index] += 1;
        }
        let mut total = 0;
        for h in (0..buckets.len()).rev() {
            total += buckets[h];
            if total >= h {
                return h as i32;
            }
        }
        0
    }
}
