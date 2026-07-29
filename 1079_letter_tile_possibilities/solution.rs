// LeetCode 1079 - Letter Tile Possibilities
// https://leetcode.com/problems/letter-tile-possibilities/

impl Solution {
    pub fn num_tile_possibilities(tiles: String) -> i32 {
        let mut count = [0i32; 26];
        for b in tiles.bytes() {
            count[(b - b'A') as usize] += 1;
        }
        Self::dfs(&mut count)
    }

    fn dfs(count: &mut [i32; 26]) -> i32 {
        let mut total = 0;
        for i in 0..26 {
            if count[i] == 0 {
                continue;
            }
            count[i] -= 1;
            total += 1 + Self::dfs(count);
            count[i] += 1;
        }
        total
    }
}
