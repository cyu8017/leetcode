// LeetCode 1053 - Previous Permutation With One Swap
// https://leetcode.com/problems/previous-permutation-with-one-swap/

impl Solution {
    pub fn prev_perm_opt1(mut arr: Vec<i32>) -> Vec<i32> {
        let n = arr.len();
        let mut i = n as i32 - 2;
        while i >= 0 && arr[i as usize] <= arr[i as usize + 1] {
            i -= 1;
        }
        if i < 0 {
            return arr;
        }
        let i = i as usize;
        let mut j = n - 1;
        while arr[j] >= arr[i] || arr[j] == arr[j - 1] {
            j -= 1;
        }
        arr.swap(i, j);
        arr
    }
}
