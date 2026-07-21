// LeetCode 1896 - Minimum Cost to Change the Final Value of Expression
// https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/

impl Solution {
    pub fn min_operations_to_flip(expression: String) -> i32 {
        let bytes = expression.as_bytes();
        let mut index = 0usize;

        fn combine(left: [i32; 3], op: u8, right: [i32; 3]) -> [i32; 3] {
            let [left_val, left_to_zero, left_to_one] = left;
            let [right_val, right_to_zero, right_to_one] = right;
            if op == b'&' {
                let and_val = left_val & right_val;
                let and_to_zero = left_to_zero.min(left_to_one + right_to_zero);
                let and_to_one = left_to_one + right_to_one;
                let or_to_zero = left_to_zero + right_to_zero;
                let or_to_one = left_to_one
                    .min(left_to_zero + right_to_one)
                    .min(right_to_zero + left_to_one);
                [
                    and_val,
                    and_to_zero.min(1 + or_to_zero),
                    and_to_one.min(1 + or_to_one),
                ]
            } else {
                let or_val = left_val | right_val;
                let or_to_zero = left_to_zero + right_to_zero;
                let or_to_one = left_to_one
                    .min(left_to_zero + right_to_one)
                    .min(right_to_zero + left_to_one);
                let and_to_zero = left_to_zero.min(left_to_one + right_to_zero);
                let and_to_one = left_to_one + right_to_one;
                [
                    or_val,
                    or_to_zero.min(1 + and_to_zero),
                    or_to_one.min(1 + and_to_one),
                ]
            }
        }

        fn parse_factor(bytes: &[u8], index: &mut usize) -> [i32; 3] {
            if bytes[*index] == b'0' || bytes[*index] == b'1' {
                let value = (bytes[*index] - b'0') as i32;
                *index += 1;
                return [
                    value,
                    if value == 0 { 0 } else { 1 },
                    if value == 0 { 1 } else { 0 },
                ];
            }
            *index += 1;
            let node = parse_expr(bytes, index);
            *index += 1;
            node
        }

        fn parse_expr(bytes: &[u8], index: &mut usize) -> [i32; 3] {
            let mut node = parse_factor(bytes, index);
            while *index < bytes.len() && (bytes[*index] == b'&' || bytes[*index] == b'|') {
                let op = bytes[*index];
                *index += 1;
                node = combine(node, op, parse_factor(bytes, index));
            }
            node
        }

        let [value, to_zero, to_one] = parse_expr(bytes, &mut index);
        if value != 0 {
            to_zero
        } else {
            to_one
        }
    }
}
