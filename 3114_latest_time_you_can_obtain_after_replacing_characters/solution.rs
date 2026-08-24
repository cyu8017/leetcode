// LeetCode 3114 - Latest Time You Can Obtain After Replacing Characters
// https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/

impl Solution {
    pub fn find_latest_time(s: String) -> String {
        let sb = s.as_bytes();
        for h in (0..=11).rev() {
            for m in (0..=59).rev() {
                let t = format!("{:02}:{:02}", h, m);
                let tb = t.as_bytes();
                let mut ok = true;
                for i in 0..5 {
                    if sb[i] != b'?' && sb[i] != tb[i] {
                        ok = false;
                        break;
                    }
                }
                if ok {
                    return t;
                }
            }
        }
        String::new()
    }
}
