// LeetCode 3861 - Minimum Capacity Box
// https://leetcode.com/problems/minimum-capacity-box/

impl Solution {
    pub fn minimum_index(capacity: Vec<i32>, item_size: i32) -> i32 {
        let mut ans = -1;
        for (i, &c) in capacity.iter().enumerate() {
            if c >= item_size && (ans == -1 || c < capacity[ans as usize]) {
                ans = i as i32;
            }
        }
        ans
    }
}
