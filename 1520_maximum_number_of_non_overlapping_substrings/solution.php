<?php

class Solution {
    /**
     * @param String $s
     * @return String[]
     */
    function maxNumOfSubstrings($s) {
        $first = [];
        $last = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if (!isset($first[$ch])) {
                $first[$ch] = $i;
            }
            $last[$ch] = $i;
        }
        $intervals = [];
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if ($first[$ch] !== $i) {
                continue;
            }
            $end = $last[$ch];
            $j = $i;
            $valid = true;
            while ($j <= $end) {
                if ($first[$s[$j]] < $i) {
                    $valid = false;
                    break;
                }
                $end = max($end, $last[$s[$j]]);
                $j++;
            }
            if ($valid) {
                $intervals[] = [$end, $i];
            }
        }
        usort($intervals, function ($a, $b) {
            return $a[0] <=> $b[0];
        });
        $answer = [];
        $previousEnd = -1;
        foreach ($intervals as $interval) {
            [$end, $start] = $interval;
            if ($start > $previousEnd) {
                $answer[] = substr($s, $start, $end - $start + 1);
                $previousEnd = $end;
            }
        }
        usort($answer, function ($a, $b) {
            return strlen($a) <=> strlen($b);
        });
        return $answer;
    }
}
