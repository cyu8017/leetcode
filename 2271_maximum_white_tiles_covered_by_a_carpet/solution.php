<?php
// LeetCode 2271 - Maximum White Tiles Covered by a Carpet
// https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

class Solution {
    function maximumWhiteTiles($tiles, $carpetLen) {
        usort($tiles, function($a, $b) { return $a[0] <=> $b[0]; });
        $n = count($tiles);
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] + ($tiles[$i][1] - $tiles[$i][0] + 1);
        $ans = 0;
        $j = 0;
        for ($i = 0; $i < $n; $i++) {
            $end = $tiles[$i][0] + $carpetLen - 1;
            while ($j < $n && $tiles[$j][0] <= $end) $j++;
            $cover = $pref[$j] - $pref[$i];
            if ($j > 0 && $tiles[$j - 1][1] > $end) $cover -= $tiles[$j - 1][1] - $end;
            $ans = max($ans, $cover);
        }
        return $ans;
    }
}
