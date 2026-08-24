// LeetCode 3260 - Find the Largest Palindrome Divisible by K
// https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/

impl Solution {
    fn strings_repeat8(n: i32) -> String {
        "8".repeat(n as usize)
    }

    fn mod7(s: &str) -> i32 {
        let mut r = 0;
        for c in s.bytes() {
            r = (r * 10 + (c - b'0') as i32) % 7;
        }
        r
    }

    fn largest_pal7(n: i32) -> String {
        let half_len = ((n + 1) / 2) as usize;
        let mut half = vec![b'9'; half_len];
        loop {
            let mut pal = vec![b'0'; n as usize];
            for i in 0..half_len {
                pal[i] = half[i];
            }
            for i in 0..(n as usize / 2) {
                pal[n as usize - 1 - i] = pal[i];
            }
            let pal_s = String::from_utf8(pal).unwrap();
            if Self::mod7(&pal_s) == 0 {
                return pal_s;
            }
            let mut i = half_len as i32 - 1;
            while i >= 0 && half[i as usize] == b'0' {
                half[i as usize] = b'9';
                i -= 1;
            }
            if i < 0 {
                break;
            }
            half[i as usize] -= 1;
        }
        String::new()
    }

    pub fn largest_palindrome(n: i32, k: i32) -> String {
        let mut digits = vec![b'9'; n as usize];
        let half = ((n + 1) / 2) as usize;
        match k {
            1 | 3 | 9 => String::from_utf8(digits).unwrap(),
            2 => {
                digits[0] = b'8';
                digits[n as usize - 1] = b'8';
                String::from_utf8(digits).unwrap()
            }
            4 => {
                if n == 1 {
                    return "8".to_string();
                }
                digits[0] = b'8';
                digits[1] = b'8';
                digits[n as usize - 1] = b'8';
                digits[n as usize - 2] = b'8';
                String::from_utf8(digits).unwrap()
            }
            5 => {
                digits[0] = b'5';
                digits[n as usize - 1] = b'5';
                String::from_utf8(digits).unwrap()
            }
            8 => {
                if n <= 2 {
                    return Self::strings_repeat8(n);
                }
                digits[0] = b'8';
                digits[1] = b'8';
                digits[2] = b'8';
                digits[n as usize - 1] = b'8';
                digits[n as usize - 2] = b'8';
                digits[n as usize - 3] = b'8';
                String::from_utf8(digits).unwrap()
            }
            6 => {
                if n == 1 {
                    return "6".to_string();
                }
                digits[0] = b'8';
                digits[n as usize - 1] = b'8';
                let sum = 16 + 9 * (n - 2);
                let need = sum % 3;
                if need != 0 {
                    let pos = half - 1;
                    digits[pos] = (digits[pos] - need as u8) as u8;
                    if n % 2 == 0 || pos != n as usize - 1 - pos {
                        digits[n as usize - 1 - pos] = digits[pos];
                    }
                }
                String::from_utf8(digits).unwrap()
            }
            7 => Self::largest_pal7(n),
            _ => String::from_utf8(digits).unwrap(),
        }
    }
}
