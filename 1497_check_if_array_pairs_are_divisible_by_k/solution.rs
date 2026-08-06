// LeetCode 1497 - Check If Array Pairs Are Divisible by k
// https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

impl Solution {
    pub fn can_arrange(arr: Vec<i32>, k: i32) -> bool {
        let mut count = vec![0i32; k as usize];
        for x in arr {
            let r = ((x % k) + k) % k;
            count[r as usize] += 1;
        }
        if count[0] % 2 != 0 {
            return false;
        }
        for r in 1..k {
            if count[r as usize] != count[(k - r) as usize] {
                return false;
            }
        }
        true
    }
}
