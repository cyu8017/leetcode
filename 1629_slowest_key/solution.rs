// LeetCode 1629 - Slowest Key
// https://leetcode.com/problems/slowest-key/

impl Solution {
    pub fn slowest_key(release_times: Vec<i32>, keys_pressed: String) -> char {
        let keys: Vec<u8> = keys_pressed.into_bytes();
        let mut best_dur = release_times[0];
        let mut best_key = keys[0];
        for i in 1..release_times.len() {
            let dur = release_times[i] - release_times[i - 1];
            if dur > best_dur || (dur == best_dur && keys[i] > best_key) {
                best_dur = dur;
                best_key = keys[i];
            }
        }
        best_key as char
    }
}
