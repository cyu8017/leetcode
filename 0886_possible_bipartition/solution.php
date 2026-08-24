<?php
// LeetCode 0886 - Possible Bipartition
// https://leetcode.com/problems/possible-bipartition/

class Solution {
    function possibleBipartition($n, $dislikes) {
        $graph = array_fill(0, $n + 1, []);
        foreach ($dislikes as $e) {
            $graph[$e[0]][] = $e[1];
            $graph[$e[1]][] = $e[0];
        }
        $color = [];
        for ($start = 1; $start <= $n; $start++) {
            if (array_key_exists($start, $color)) continue;
            $queue = [$start];
            $color[$start] = 0;
            while ($queue) {
                $node = array_shift($queue);
                foreach ($graph[$node] as $nei) {
                    if (!array_key_exists($nei, $color)) {
                        $color[$nei] = $color[$node] ^ 1;
                        $queue[] = $nei;
                    } elseif ($color[$nei] === $color[$node]) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}
