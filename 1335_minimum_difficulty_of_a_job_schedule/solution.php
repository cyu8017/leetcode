<?php
class Solution {
    function minDifficulty($jobDifficulty, $d) {
        $n = count($jobDifficulty);
        if ($n < $d) return -1;
        $dp = array_fill(0, $n, 1000000000);
        $hardest = 0;
        for ($i = 0; $i < $n; $i++) {
            $hardest = max($hardest, $jobDifficulty[$i]);
            $dp[$i] = $hardest;
        }
        for ($day = 1; $day < $d; $day++) {
            $nxt = array_fill(0, $n, 1000000000);
            for ($end = $day; $end < $n; $end++) {
                $hardest = 0;
                for ($start = $end; $start >= $day; $start--) {
                    $hardest = max($hardest, $jobDifficulty[$start]);
                    $nxt[$end] = min($nxt[$end], $dp[$start - 1] + $hardest);
                }
            }
            $dp = $nxt;
        }
        return $dp[$n - 1];
    }
}
