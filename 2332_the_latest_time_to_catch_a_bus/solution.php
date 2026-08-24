<?php
// LeetCode 2332 - The Latest Time to Catch a Bus
// https://leetcode.com/problems/the-latest-time-to-catch-a-bus/

class Solution {
    function latestTimeCatchTheBus($buses, $passengers, $capacity) {
        sort($buses);
        sort($passengers);
        $pos = 0;
        $bn = count($buses);
        $pn = count($passengers);
        for ($bi = 0; $bi < $bn; $bi++) {
            $bus = $buses[$bi];
            $cap = $capacity;
            while ($cap > 0 && $pos < $pn && $passengers[$pos] <= $bus) {
                $pos++;
                $cap--;
            }
            if ($bi === $bn - 1) {
                $cand = $bus;
                if ($cap === 0) $cand = $passengers[$pos - 1];
                $taken = [];
                foreach ($passengers as $p) $taken[$p] = true;
                while (isset($taken[$cand])) $cand--;
                return $cand;
            }
        }
        return -1;
    }
}
