struct Solution;
// LeetCode 3468 - Find the Number of Copy Arrays
// https://leetcode.com/problems/find-the-number-of-copy-arrays/

impl Solution {
    pub fn count_arrays(original: Vec<i32>, bounds: Vec<Vec<i32>>) -> i32 {
        let n = original.len();
        let mut lo = bounds[0][0];
        let mut hi = bounds[0][1];
        for i in 1..n {
            let diff = original[i] - original[i - 1];
            let lo2 = bounds[i][0];
            let hi2 = bounds[i][1];
            let mut nlo = lo + diff;
            let mut nhi = hi + diff;
            if nlo < lo2 {
                nlo = lo2;
            }
            if nhi > hi2 {
                nhi = hi2;
            }
            if nlo > nhi {
                return 0;
            }
            lo = nlo;
            hi = nhi;
        }
        hi - lo + 1
    }
}

fn main() {}
