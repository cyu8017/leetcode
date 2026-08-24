// LeetCode 0937 - Reorder Data in Log Files
// https://leetcode.com/problems/reorder-data-in-log-files/

impl Solution {
    pub fn reorder_log_files(mut logs: Vec<String>) -> Vec<String> {
        logs.sort_by(|a, b| {
            let spa = a.find(' ').unwrap();
            let spb = b.find(' ').unwrap();
            let resta = &a[spa + 1..];
            let restb = &b[spb + 1..];
            let letter_a = resta.as_bytes()[0].is_ascii_alphabetic();
            let letter_b = restb.as_bytes()[0].is_ascii_alphabetic();
            match (letter_a, letter_b) {
                (true, true) => {
                    let cmp = resta.cmp(restb);
                    if cmp != std::cmp::Ordering::Equal {
                        cmp
                    } else {
                        a[..spa].cmp(&b[..spb])
                    }
                }
                (true, false) => std::cmp::Ordering::Less,
                (false, true) => std::cmp::Ordering::Greater,
                (false, false) => std::cmp::Ordering::Equal,
            }
        });
        logs
    }
}
