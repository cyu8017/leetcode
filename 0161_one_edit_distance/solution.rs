// LeetCode 0161 - One Edit Distance
impl Solution {
    pub fn is_one_edit_distance(s: String, t: String) -> bool {
        let (s, t) = if s.len() > t.len() { (t, s) } else { (s, t) };
        if t.len() - s.len() > 1 || s == t { return false; }
        let (a, b) = (s.as_bytes(), t.as_bytes());
        let mut i = 0;
        while i < a.len() && a[i] == b[i] { i += 1; }
        if a.len() == b.len() { a[i + 1..] == b[i + 1..] } else { a[i..] == b[i + 1..] }
    }
}