// LeetCode 2232 - Minimize Result by Adding Parentheses to Expression
// https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

impl Solution {
    pub fn minimize_result(expression: String) -> String {
        let plus = expression.find('+').unwrap();
        let left = &expression[..plus];
        let right = &expression[plus + 1..];
        let mut best_val = i32::MAX;
        let mut best = String::new();
        for i in 0..left.len() {
            for j in 1..=right.len() {
                let a = &left[..i];
                let b = &left[i..];
                let c = &right[..j];
                let d = &right[j..];
                let mut val = b.parse::<i32>().unwrap() + c.parse::<i32>().unwrap();
                if !a.is_empty() {
                    val *= a.parse::<i32>().unwrap();
                }
                if !d.is_empty() {
                    val *= d.parse::<i32>().unwrap();
                }
                if val < best_val {
                    best_val = val;
                    best = format!("{a}({b}+{c}){d}");
                }
            }
        }
        best
    }
}
