<?php
// LeetCode 3948 - Lexicographically Maximum MEX Array
// https://leetcode.com/problems/lexicographically-maximum-mex-array/

class Solution {
    function maxMexArray($nums) {
        $n = count($nums);
        $remaining = array_fill(0, $n + 2, 0);
        foreach ($nums as $x) {
            if ($x <= $n + 1) $remaining[$x]++;
        }
        $mex = 0;
        while ($remaining[$mex] > 0) $mex++;
        $answer = [];
        $seen = array_fill(0, $n + 2, 0);
        $stamp = 0;
        $index = 0;
        while ($index < $n) {
            if ($mex === 0) {
                $answer[] = 0;
                $x = $nums[$index];
                if ($x <= $n + 1) $remaining[$x]--;
                $index++;
                continue;
            }
            $stamp++;
            $need = $mex;
            while ($need > 0) {
                $x = $nums[$index];
                if ($x < $mex && $seen[$x] !== $stamp) {
                    $seen[$x] = $stamp;
                    $need--;
                }
                if ($x <= $n + 1) $remaining[$x]--;
                $index++;
            }
            $answer[] = $mex;
            $mex = 0;
            while ($remaining[$mex] > 0) $mex++;
        }
        return $answer;
    }
}
