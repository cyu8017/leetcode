// LeetCode 1860 - Incremental Memory Leak
// https://leetcode.com/problems/incremental-memory-leak/

impl Solution {
    pub fn mem_leak(mut memory1: i32, mut memory2: i32) -> Vec<i32> {
        let mut second = 1i32;
        while memory1 >= second || memory2 >= second {
            if memory1 >= memory2 {
                memory1 -= second;
            } else {
                memory2 -= second;
            }
            second += 1;
        }
        vec![second, memory1, memory2]
    }
}
