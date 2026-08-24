// LeetCode 3076 - Shortest Uncommon Substring in an Array
// https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/

impl Solution {
    pub fn shortest_substrings(arr: Vec<String>) -> Vec<String> {
        let n = arr.len();
        let mut ans = vec![String::new(); n];
        for i in 0..n {
            let s = arr[i].as_bytes();
            let m = s.len();
            let mut j = 1;
            while j <= m && ans[i].is_empty() {
                for l in 0..=m - j {
                    let sub = std::str::from_utf8(&s[l..l + j]).unwrap();
                    if ans[i].is_empty() || ans[i].as_str() > sub {
                        let mut ok = true;
                        for k in 0..n {
                            if k != i && arr[k].contains(sub) {
                                ok = false;
                                break;
                            }
                        }
                        if ok {
                            ans[i] = sub.to_string();
                        }
                    }
                }
                j += 1;
            }
        }
        ans
    }
}
