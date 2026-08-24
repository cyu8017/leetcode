// LeetCode 2705 - Compact Object
// https://leetcode.com/problems/compact-object/

impl Solution {
    pub fn compact_object(obj: Vec<i32>) -> Vec<i32> {
        obj.into_iter().filter(|&x| x != 0).collect()
    }
}
