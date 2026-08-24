<?php
// LeetCode 0963 - Minimum Area Rectangle II
// https://leetcode.com/problems/minimum-area-rectangle-ii/

class Solution {
    function minAreaFreeRect($points) {
        $n = count($points);
        $groups = [];
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $cx = $points[$i][0] + $points[$j][0];
                $cy = $points[$i][1] + $points[$j][1];
                $dx = $points[$i][0] - $points[$j][0];
                $dy = $points[$i][1] - $points[$j][1];
                $dist = $dx * $dx + $dy * $dy;
                $key = $cx . "#" . $cy . "#" . $dist;
                $groups[$key][] = [$i, $j];
            }
        }
        $ans = 1e300;
        foreach ($groups as $pairs) {
            $m = count($pairs);
            for ($a = 0; $a < $m; $a++) {
                for ($b = $a + 1; $b < $m; $b++) {
                    $p1 = $pairs[$a][0];
                    $p2 = $pairs[$b][0];
                    $q2 = $pairs[$b][1];
                    $d1 = hypot($points[$p1][0] - $points[$p2][0], $points[$p1][1] - $points[$p2][1]);
                    $d2 = hypot($points[$p1][0] - $points[$q2][0], $points[$p1][1] - $points[$q2][1]);
                    $area = $d1 * $d2;
                    if ($area > 0) $ans = min($ans, $area);
                }
            }
        }
        return $ans >= 1e299 ? 0.0 : $ans;
    }
}
