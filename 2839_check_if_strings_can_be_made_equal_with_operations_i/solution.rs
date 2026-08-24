// LeetCode 2839 - Check if Strings Can be Made Equal With Operations I
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

impl Solution {
    pub fn can_be_equal(s1: String, s2: String) -> bool {
        let a: Vec<u8> = s1.bytes().collect();
        let b: Vec<u8> = s2.bytes().collect();
        let mut even1 = [a[0], a[2]];
        let mut even2 = [b[0], b[2]];
        let mut odd1 = [a[1], a[3]];
        let mut odd2 = [b[1], b[3]];
        even1.sort_unstable();
        even2.sort_unstable();
        odd1.sort_unstable();
        odd2.sort_unstable();
        even1 == even2 && odd1 == odd2
    }
}
