// LeetCode 0514 - Freedom Trail
// https://leetcode.com/problems/freedom-trail/

use std::collections::HashMap;

impl Solution {
    fn dp(
        ring_index: i32,
        key_index: i32,
        ring: &[u8],
        key: &[u8],
        positions: &HashMap<u8, Vec<i32>>,
        memo: &mut HashMap<(i32, i32), i32>,
    ) -> i32 {
        if key_index as usize == key.len() {
            return 0;
        }
        if let Some(&value) = memo.get(&(ring_index, key_index)) {
            return value;
        }

        let ring_len = ring.len() as i32;
        let mut best = i32::MAX;
        for &pos in positions.get(&key[key_index as usize]).unwrap() {
            let clockwise = (pos - ring_index + ring_len) % ring_len;
            let counter = (ring_index - pos + ring_len) % ring_len;
            let steps = clockwise.min(counter) + 1;
            best = best.min(steps + Self::dp(pos, key_index + 1, ring, key, positions, memo));
        }
        memo.insert((ring_index, key_index), best);
        best
    }

    pub fn find_rotate_steps(ring: String, key: String) -> i32 {
        let ring_bytes = ring.as_bytes();
        let key_bytes = key.as_bytes();
        let mut positions: HashMap<u8, Vec<i32>> = HashMap::new();
        for (index, &ch) in ring_bytes.iter().enumerate() {
            positions.entry(ch).or_default().push(index as i32);
        }
        let mut memo = HashMap::new();
        Self::dp(0, 0, ring_bytes, key_bytes, &positions, &mut memo)
    }
}
