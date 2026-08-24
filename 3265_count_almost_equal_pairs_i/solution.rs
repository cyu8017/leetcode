// LeetCode 3265 - Count Almost Equal Pairs I
// https://leetcode.com/problems/count-almost-equal-pairs-i/

impl Solution {
    fn sprintf_num(mut x: i32) -> String {
        if x == 0 {
            return "0".to_string();
        }
        let mut b = String::new();
        while x > 0 {
            b.insert(0, char::from(b'0' + (x % 10) as u8));
            x /= 10;
        }
        b
    }

    fn almost_equal(a: i32, b: i32) -> bool {
        let mut sa = Self::sprintf_num(a);
        let mut sb = Self::sprintf_num(b);
        while sa.len() < sb.len() {
            sa.insert(0, '0');
        }
        while sb.len() < sa.len() {
            sb.insert(0, '0');
        }
        let mut diff = Vec::new();
        for i in 0..sa.len() {
            if sa.as_bytes()[i] != sb.as_bytes()[i] {
                diff.push(i);
            }
        }
        if diff.is_empty() {
            return true;
        }
        if diff.len() != 2 {
            return false;
        }
        let i = diff[0];
        let j = diff[1];
        sa.as_bytes()[i] == sb.as_bytes()[j] && sa.as_bytes()[j] == sb.as_bytes()[i]
    }

    pub fn count_pairs(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        for i in 0..nums.len() {
            for j in i + 1..nums.len() {
                if Self::almost_equal(nums[i], nums[j]) {
                    ans += 1;
                }
            }
        }
        ans
    }
}
