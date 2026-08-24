// LeetCode 2933 - High-Access Employees
// https://leetcode.com/problems/high-access-employees/

use std::collections::HashMap;

impl Solution {
    pub fn find_high_access_employees(access_times: Vec<Vec<String>>) -> Vec<String> {
        let mut m: HashMap<String, Vec<i32>> = HashMap::new();
        for a in access_times {
            let name = a[0].clone();
            let t = a[1].as_bytes();
            let hh = (t[0] - b'0') as i32 * 10 + (t[1] - b'0') as i32;
            let mm = (t[2] - b'0') as i32 * 10 + (t[3] - b'0') as i32;
            m.entry(name).or_default().push(hh * 60 + mm);
        }
        let mut ans = Vec::new();
        for (name, times) in m.iter_mut() {
            times.sort_unstable();
            for i in 0..times.len().saturating_sub(2) {
                if times[i + 2] - times[i] < 60 {
                    ans.push(name.clone());
                    break;
                }
            }
        }
        ans.sort();
        ans
    }
}
