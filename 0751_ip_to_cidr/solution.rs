// LeetCode 0751 - IP to CIDR
// https://leetcode.com/problems/ip-to-cidr/

impl Solution {
    pub fn ip_to_cidr(ip: String, mut n: i32) -> Vec<String> {
        let mut start = Self::ip_to_int(&ip);
        let mut answer = Vec::new();
        while n > 0 {
            let mut lowbit = if start == 0 { 1i64 << 32 } else { start & -start };
            while lowbit > n as i64 {
                lowbit >>= 1;
            }
            let mask = 32 - (Self::bit_length(lowbit) - 1);
            answer.push(format!("{}/{}", Self::int_to_ip(start), mask));
            start += lowbit;
            n -= lowbit as i32;
        }
        answer
    }

    fn ip_to_int(value: &str) -> i64 {
        value
            .split('.')
            .fold(0i64, |acc, part| acc * 256 + part.parse::<i64>().unwrap())
    }

    fn int_to_ip(value: i64) -> String {
        format!(
            "{}.{}.{}.{}",
            (value >> 24) & 255,
            (value >> 16) & 255,
            (value >> 8) & 255,
            value & 255
        )
    }

    fn bit_length(mut value: i64) -> i32 {
        let mut len = 0;
        while value != 0 {
            value >>= 1;
            len += 1;
        }
        len
    }
}
