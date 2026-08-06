<?php
class Solution {
    function minimumDistance($word) {
        $distance = function($a, $b) {
            if ($a === 26) return 0;
            return abs(intdiv($a, 6) - intdiv($b, 6)) + abs($a % 6 - $b % 6);
        };
        $letters = [];
        for ($i = 0; $i < strlen($word); $i++) $letters[] = ord($word[$i]) - 65;
        $dp = [26 => 0];
        $previous = $letters[0];
        for ($idx = 1; $idx < count($letters); $idx++) {
            $current = $letters[$idx];
            $nxt = [];
            foreach ($dp as $free => $cost) {
                $v1 = $cost + $distance($previous, $current);
                $nxt[$free] = min($nxt[$free] ?? PHP_INT_MAX, $v1);
                $v2 = $cost + $distance($free, $current);
                $nxt[$previous] = min($nxt[$previous] ?? PHP_INT_MAX, $v2);
            }
            $dp = $nxt;
            $previous = $current;
        }
        return min($dp);
    }
}
