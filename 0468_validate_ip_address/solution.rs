// LeetCode 0468 - Validate IP Address
// https://leetcode.com/problems/validate-ip-address/

impl Solution {
    fn is_ipv4(address: &str) -> bool {
        let parts: Vec<&str> = address.split('.').collect();
        if parts.len() != 4 {
            return false;
        }
        for part in parts {
            if part.is_empty() || part.len() > 3 {
                return false;
            }
            if part.len() > 1 && part.starts_with('0') {
                return false;
            }
            if !part.chars().all(|ch| ch.is_ascii_digit()) {
                return false;
            }
            let value: i32 = part.parse().unwrap_or(256);
            if value > 255 {
                return false;
            }
        }
        true
    }

    fn is_ipv6(address: &str) -> bool {
        let parts: Vec<&str> = address.split(':').collect();
        if parts.len() != 8 {
            return false;
        }
        for part in parts {
            if part.is_empty() || part.len() > 4 {
                return false;
            }
            if !part
                .chars()
                .all(|ch| ch.is_ascii_digit() || matches!(ch, 'a'..='f' | 'A'..='F'))
            {
                return false;
            }
        }
        true
    }

    pub fn valid_ipaddress(query_ip: String) -> String {
        if Self::is_ipv4(&query_ip) {
            return "IPv4".to_string();
        }
        if Self::is_ipv6(&query_ip) {
            return "IPv6".to_string();
        }
        "Neither".to_string()
    }
}
