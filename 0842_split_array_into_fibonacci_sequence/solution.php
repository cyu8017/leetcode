<?php
// LeetCode 0842 - Split Array into Fibonacci Sequence
// https://leetcode.com/problems/split-array-into-fibonacci-sequence/

class Solution {
    /**
     * @param String $num
     * @return Integer[]
     */
    function splitIntoFibonacci($num) {
        $path = [];
        $dfs = function($start) use (&$dfs, $num, &$path) {
            $n = strlen($num);
            if ($start === $n) return count($path) >= 3;
            $val = 0;
            for ($end = $start; $end < $n; $end++) {
                if ($num[$start] === '0' && $end > $start) break;
                $val = $val * 10 + (ord($num[$end]) - 48);
                if ($val > 2147483647) break;
                if (count($path) >= 2) {
                    $total = $path[count($path) - 1] + $path[count($path) - 2];
                    if ($val < $total) continue;
                    if ($val > $total) break;
                }
                $path[] = $val;
                if ($dfs($end + 1)) return true;
                array_pop($path);
            }
            return false;
        };
        $dfs(0);
        return $path;
    }
}
