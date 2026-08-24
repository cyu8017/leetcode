// LeetCode 2840 - Check if Strings Can be Made Equal With Operations II
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/

impl Solution {
    pub fn check_strings(s1: String, s2: String) -> bool {
        let mut even1 = [0i32; 26];
        let mut odd1 = [0i32; 26];
        let mut even2 = [0i32; 26];
        let mut odd2 = [0i32; 26];
        for (i, (c1, c2)) in s1.bytes().zip(s2.bytes()).enumerate() {
            if i % 2 == 0 {
                even1[(c1 - b'a') as usize] += 1;
                even2[(c2 - b'a') as usize] += 1;
            } else {
                odd1[(c1 - b'a') as usize] += 1;
                odd2[(c2 - b'a') as usize] += 1;
            }
        }
        even1 == even2 && odd1 == odd2
    }
}
