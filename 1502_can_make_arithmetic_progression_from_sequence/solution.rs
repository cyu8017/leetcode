// LeetCode 1502 - Can Make Arithmetic Progression From Sequence
// https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

impl Solution {
    pub fn can_make_arithmetic_progression(mut arr: Vec<i32>) -> bool {
        arr.sort_unstable();
        let diff = arr[1] - arr[0];
        for i in 2..arr.len() {
            if arr[i] - arr[i - 1] != diff {
                return false;
            }
        }
        true
    }
}
