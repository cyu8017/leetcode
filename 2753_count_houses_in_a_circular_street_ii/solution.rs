// LeetCode 2753 - Count Houses in a Circular Street II
// https://leetcode.com/problems/count-houses-in-a-circular-street-ii/

impl Solution {
    pub fn house_count(street: Vec<i32>, k: i32) -> i32 {
        let n = street.len();
        if n == 0 {
            return 0;
        }
        let start = match street.iter().position(|&v| v == 1) {
            Some(i) => i,
            None => return 0,
        };
        let mut count = 1;
        let mut moves = 0;
        let mut i = start;
        while moves < k {
            i = (i + 1) % n;
            moves += 1;
            if i == start {
                break;
            }
            if street[i] == 1 {
                count += 1;
            }
        }
        count
    }
}
