// LeetCode 0165 - Compare Version Numbers
impl Solution {
    pub fn compare_version(version1: String, version2: String) -> i32 {
        let (mut a, mut b) = (version1.split('.'), version2.split('.'));
        loop {
            match (a.next(), b.next()) {
                (None, None) => return 0,
                (x, y) => {
                    let left: i32 = x.unwrap_or("0").parse().unwrap();
                    let right: i32 = y.unwrap_or("0").parse().unwrap();
                    if left != right { return if left < right { -1 } else { 1 }; }
                }
            }
        }
    }
}