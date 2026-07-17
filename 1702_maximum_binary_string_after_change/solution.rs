// LeetCode 1702 - Maximum Binary String After Change
// https://leetcode.com/problems/maximum-binary-string-after-change/

impl Solution {
    pub fn maximum_binary_string(binary: String) -> String {
        let zeros = binary.bytes().filter(|&b| b == b'0').count();
        if zeros <= 1 {
            return binary;
        }
        let first = binary.find('0').unwrap();
        let n = binary.len();
        format!(
            "{}0{}",
            "1".repeat(first + zeros - 1),
            "1".repeat(n - first - zeros)
        )
    }
}
