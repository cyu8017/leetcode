<?php
// LeetCode 3753 - Total Waviness of Numbers in Range II
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

class Solution {
    function totalWaviness($a, $b) {
        $wavinessUpTo = function($limit) {
            if ($limit < 0) return 0;
            $digits = [];
            if ($limit === 0) $digits[] = 0;
            else {
                for ($value = $limit; $value > 0; $value = intdiv($value, 10))
                    $digits[] = $value % 10;
                $digits = array_reverse($digits);
            }
            $memo = [];
            $dfs = function($position, $secondLast, $last, $started, $tight) use (&$dfs, &$memo, $digits) {
                if ($position === count($digits)) return ['count' => 1, 'sum' => 0];
                $key = $position . "," . $secondLast . "," . $last . "," . ($started ? 1 : 0);
                if (!$tight && isset($memo[$key])) return $memo[$key];
                $upper = $tight ? $digits[$position] : 9;
                $result = ['count' => 0, 'sum' => 0];
                for ($digit = 0; $digit <= $upper; $digit++) {
                    $nextTight = $tight && $digit === $upper;
                    $nextSecondLast = $secondLast;
                    $nextLast = $last;
                    $nextStarted = $started || $digit !== 0;
                    $add = 0;
                    if (!$nextStarted) {
                        $nextSecondLast = $nextLast = 10;
                    } else if (!$started) {
                        $nextSecondLast = 10;
                        $nextLast = $digit;
                    } else {
                        if ($secondLast !== 10 &&
                            (($last > $secondLast && $last > $digit) || ($last < $secondLast && $last < $digit))) {
                            $add = 1;
                        }
                        $nextSecondLast = $last;
                        $nextLast = $digit;
                    }
                    $child = $dfs($position + 1, $nextSecondLast, $nextLast, $nextStarted, $nextTight);
                    $result['count'] += $child['count'];
                    $result['sum'] += $child['sum'] + $add * $child['count'];
                }
                if (!$tight) $memo[$key] = $result;
                return $result;
            };
            return $dfs(0, 10, 10, false, true)['sum'];
        };
        return $wavinessUpTo($b) - $wavinessUpTo($a - 1);
    }
}
