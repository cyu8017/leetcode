// LeetCode 2271 - Maximum White Tiles Covered by a Carpet
// https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

impl Solution {
    pub fn maximum_white_tiles(mut tiles: Vec<Vec<i32>>, carpet_len: i32) -> i32 {
        tiles.sort_unstable();
        let n = tiles.len();
        let mut pref = vec![0i32; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + (tiles[i][1] - tiles[i][0] + 1);
        }
        let mut ans = 0;
        let mut j = 0;
        for i in 0..n {
            let end = tiles[i][0] + carpet_len - 1;
            while j < n && tiles[j][0] <= end {
                j += 1;
            }
            let mut cover = pref[j] - pref[i];
            if j > 0 && tiles[j - 1][1] > end {
                cover -= tiles[j - 1][1] - end;
            }
            ans = ans.max(cover);
        }
        ans
    }
}
