<?php
// LeetCode 2045 - Second Minimum Time to Reach Destination
// https://leetcode.com/problems/second-minimum-time-to-reach-destination/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer $time
     * @param Integer $change
     * @return Integer
     */
    function secondMinimum($n, $edges, $time, $change) {
        $g = array_fill(0, $n + 1, []);
        foreach ($edges as $e) { $g[$e[0]][] = $e[1]; $g[$e[1]][] = $e[0]; }
        $dist1 = array_fill(0, $n + 1, -1);
        $dist2 = array_fill(0, $n + 1, -1);
        $q = [[1, 0]];
        $dist1[1] = 0;
        while ($q) {
            [$u, $d] = array_shift($q);
            foreach ($g[$u] as $v) {
                $nd = $d + 1;
                if ($dist1[$v] === -1) { $dist1[$v] = $nd; $q[] = [$v, $nd]; }
                else if ($dist2[$v] === -1 && $nd > $dist1[$v]) { $dist2[$v] = $nd; $q[] = [$v, $nd]; }
            }
        }
        $steps = $dist2[$n];
        $ans = 0;
        for ($i = 0; $i < $steps; $i++) {
            if (intdiv($ans, $change) % 2 === 1) $ans += $change - $ans % $change;
            $ans += $time;
        }
        return $ans;
    }
}
