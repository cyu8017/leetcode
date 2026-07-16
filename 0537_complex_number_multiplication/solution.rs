// LeetCode 0537 - Complex Number Multiplication
// https://leetcode.com/problems/complex-number-multiplication/

impl Solution {
    pub fn complex_number_multiply(num1: String, num2: String) -> String {
        fn parse(num: &str) -> (i32, i32) {
            let plus = num.find('+').unwrap();
            let real: i32 = num[..plus].parse().unwrap();
            let imag: i32 = num[plus + 1..num.len() - 1].parse().unwrap();
            (real, imag)
        }

        let (a, b) = parse(&num1);
        let (c, d) = parse(&num2);
        let real = a * c - b * d;
        let imag = a * d + b * c;
        format!("{real}+{imag}i")
    }
}
