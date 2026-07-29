// LeetCode 1071 - Greatest Common Divisor of Strings
// https://leetcode.com/problems/greatest-common-divisor-of-strings/

impl Solution {
    pub fn gcd_of_strings(str1: String, str2: String) -> String {
        if format!("{}{}", str1, str2) != format!("{}{}", str2, str1) {
            return String::new();
        }
        let g = Self::gcd(str1.len(), str2.len());
        str1[..g].to_string()
    }

    fn gcd(mut a: usize, mut b: usize) -> usize {
        while b != 0 {
            let t = b;
            b = a % b;
            a = t;
        }
        a
    }
}
