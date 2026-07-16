// LeetCode 0060 - Permutation Sequence
// https://leetcode.com/problems/permutation-sequence/

impl Solution {
    pub fn get_permutation(n: i32, k: i32) -> String {
        let n = n as usize;
        let mut k = k as i32 - 1;
        let mut numbers: Vec<i32> = (1..=n as i32).collect();
        let mut factorials = vec![1; n];

        for i in 1..n {
            factorials[i] = factorials[i - 1] * i as i32;
        }

        let mut result = String::new();

        for i in (0..n).rev() {
            let index = (k / factorials[i]) as usize;
            result.push(char::from(b'0' + numbers[index] as u8));
            numbers.remove(index);
            k %= factorials[i];
        }

        result
    }
}
