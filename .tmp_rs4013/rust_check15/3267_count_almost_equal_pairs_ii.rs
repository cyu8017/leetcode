struct Solution;
// LeetCode 3267 - Count Almost Equal Pairs II
// https://leetcode.com/problems/count-almost-equal-pairs-ii/

impl Solution {
    fn pad_num(mut x: i32) -> String {
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

    fn can_with_swaps(sa: &mut Vec<u8>, sb: &[u8], start: usize, left: i32) -> bool {
        if sa.as_slice() == sb {
            return true;
        }
        if left == 0 {
            return false;
        }
        for i in start..sa.len() {
            if sa[i] == sb[i] {
                continue;
            }
            for j in i + 1..sa.len() {
                if sa[j] == sb[i] {
                    sa.swap(i, j);
                    if Self::can_with_swaps(sa, sb, i + 1, left - 1) {
                        return true;
                    }
                    sa.swap(i, j);
                }
            }
            return false;
        }
        sa.as_slice() == sb
    }

    fn almost_equal(a: i32, b: i32) -> bool {
        let mut sa = Self::pad_num(a);
        let mut sb = Self::pad_num(b);
        while sa.len() < sb.len() {
            sa.insert(0, '0');
        }
        while sb.len() < sa.len() {
            sb.insert(0, '0');
        }
        if sa == sb {
            return true;
        }
        let mut sa_b = sa.into_bytes();
        let sb_b = sb.into_bytes();
        Self::can_with_swaps(&mut sa_b, &sb_b, 0, 2)
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

fn main() {}
