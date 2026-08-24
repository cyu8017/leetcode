// LeetCode 0763 - Partition Labels
// https://leetcode.com/problems/partition-labels/

impl Solution {
    pub fn partition_labels(s: String) -> Vec<i32> {
        let bytes = s.as_bytes();
        let mut last = [0; 26];
        for (i, &ch) in bytes.iter().enumerate() {
            last[(ch - b'a') as usize] = i;
        }
        let mut start = 0;
        let mut end = 0;
        let mut answer = Vec::new();
        for (i, &ch) in bytes.iter().enumerate() {
            end = end.max(last[(ch - b'a') as usize]);
            if i == end {
                answer.push((end - start + 1) as i32);
                start = i + 1;
            }
        }
        answer
    }
}
