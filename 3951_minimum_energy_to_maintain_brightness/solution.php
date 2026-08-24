<?php
// LeetCode 3951 - Minimum Energy To Maintain Brightness
// https://leetcode.com/problems/minimum-energy-to-maintain-brightness/

class Solution {
    function minEnergy($n, $brightness, $intervals) {
        usort($intervals, function ($a, $b) { return $a[0] <=> $b[0]; });
        $merged = [[$intervals[0][0], $intervals[0][1]]];
        for ($i = 1; $i < count($intervals); $i++) {
            $x = $intervals[$i];
            $last = count($merged) - 1;
            if ($merged[$last][1] < $x[0]) $merged[] = [$x[0], $x[1]];
            else if ($x[1] > $merged[$last][1]) $merged[$last][1] = $x[1];
        }
        $ans = 0;
        foreach ($merged as $interval) {
            $m = $interval[1] - $interval[0] + 1;
            $ans += intdiv($brightness + 2, 3) * $m;
        }
        return $ans;
    }
}
