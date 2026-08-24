<?php
// LeetCode 3323 - Minimize Connected Groups by Inserting Interval
// https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/

class Solution {
    function minConnectedGroups($intervals, $k) {
        usort($intervals, function($a, $b) { return $a[0] <=> $b[0]; });
        $merged = [];
        foreach ($intervals as $it) {
            if (!$merged || $it[0] > $merged[count($merged) - 1][1]) $merged[] = [$it[0], $it[1]];
            else if ($it[1] > $merged[count($merged) - 1][1]) $merged[count($merged) - 1][1] = $it[1];
        }
        $m = count($merged);
        $ans = $m;
        for ($i = 0; $i < $m; $i++) {
            $end = $merged[$i][1] + $k;
            $j = $i;
            while ($j < $m && $merged[$j][0] <= $end) $j++;
            $groups = $i + 1 + ($m - $j);
            if ($groups < $ans) $ans = $groups;
        }
        return $ans;
    }
}
