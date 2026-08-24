struct Solution;
// LeetCode 3388 - Count Beautiful Splits in an Array
// https://leetcode.com/problems/count-beautiful-splits-in-an-array/

impl Solution {
    fn equal(a: &[i32], as_: usize, ae: usize, bs: usize, be: usize) -> bool {
        if ae - as_ != be - bs {
            return false;
        }
        for i in 0..ae - as_ {
            if a[as_ + i] != a[bs + i] {
                return false;
            }
        }
        true
    }

    pub fn beautiful_splits(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for i in 1..n - 1 {
            for j in i + 1..n {
                let mut ok = false;
                if i <= j - i && Self::equal(&nums, 0, i, i, i + i) {
                    ok = true;
                }
                if !ok && j - i <= n - j && Self::equal(&nums, i, j, j, j + (j - i)) {
                    ok = true;
                }
                if ok {
                    ans += 1;
                }
            }
        }
        ans
    }
}

fn main() {}
