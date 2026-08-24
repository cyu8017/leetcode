<?php
// LeetCode 0920 - Number of Music Playlists
// https://leetcode.com/problems/number-of-music-playlists/

class Solution {
    function numMusicPlaylists($n, $goal, $k) {
        $MOD = 1000000007;
        $dp = [];
        for ($i = 0; $i <= $goal; $i++) $dp[$i] = array_fill(0, $n + 1, 0);
        $dp[0][0] = 1;
        for ($i = 1; $i <= $goal; $i++) {
            for ($j = 1; $j <= $i && $j <= $n; $j++) {
                $dp[$i][$j] = $dp[$i - 1][$j - 1] * ($n - $j + 1) % $MOD;
                if ($j > $k) $dp[$i][$j] = ($dp[$i][$j] + $dp[$i - 1][$j] * ($j - $k)) % $MOD;
            }
        }
        return $dp[$goal][$n];
    }
}
