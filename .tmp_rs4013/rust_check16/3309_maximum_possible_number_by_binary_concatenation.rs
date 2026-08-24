struct Solution;
// LeetCode 3309 - Maximum Possible Number by Binary Concatenation
// https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/

impl Solution {
    fn to_bin(mut x: i32) -> String {
        if x == 0 {
            return "0".to_string();
        }
        let mut s = String::new();
        while x > 0 {
            s.insert(0, if x & 1 == 1 { '1' } else { '0' });
            x >>= 1;
        }
        s
    }

    pub fn max_good_number(nums: Vec<i32>) -> i32 {
        let bs = [Self::to_bin(nums[0]), Self::to_bin(nums[1]), Self::to_bin(nums[2])];
        let mut idx = [0, 1, 2];
        let mut ans = 0;
        fn perm(i: usize, idx: &mut [usize; 3], bs: &[String; 3], ans: &mut i32) {
            if i == 3 {
                let s = format!("{}{}{}", bs[idx[0]], bs[idx[1]], bs[idx[2]]);
                let mut v = 0;
                for c in s.bytes() {
                    v = v * 2 + (c - b'0') as i32;
                }
                if v > *ans {
                    *ans = v;
                }
                return;
            }
            for j in i..3 {
                idx.swap(i, j);
                perm(i + 1, idx, bs, ans);
                idx.swap(i, j);
            }
        }
        perm(0, &mut idx, &bs, &mut ans);
        ans
    }
}

fn main() {}
