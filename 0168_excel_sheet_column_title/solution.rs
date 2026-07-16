// LeetCode 0168 - Excel Sheet Column Title
impl Solution {
    pub fn convert_to_title(mut column_number: i32) -> String {
        let mut result = Vec::new();
        while column_number > 0 {
            column_number -= 1;
            result.push(b'A' + (column_number % 26) as u8);
            column_number /= 26;
        }
        result.reverse();
        String::from_utf8(result).unwrap()
    }
}