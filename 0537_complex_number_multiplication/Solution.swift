// LeetCode 0537 - Complex Number Multiplication
// https://leetcode.com/problems/complex-number-multiplication/

class Solution {
    func complexNumberMultiply(_ num1: String, _ num2: String) -> String {
        let (a, b) = parse(num1)
        let (c, d) = parse(num2)
        let real = a * c - b * d
        let imag = a * d + b * c
        return "\(real)+\(imag)i"
    }

    private func parse(_ num: String) -> (Int, Int) {
        let parts = num.split(separator: "+", maxSplits: 1).map(String.init)
        let real = Int(parts[0])!
        let imag = Int(String(parts[1].dropLast()))!
        return (real, imag)
    }
}
