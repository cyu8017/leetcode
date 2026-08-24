<?php
// LeetCode 0838 - Push Dominoes
// https://leetcode.com/problems/push-dominoes/

class Solution {
    /**
     * @param String $dominoes
     * @return String
     */
    function pushDominoes($dominoes) {
        $arr = str_split($dominoes);
        $n = count($arr);
        $force = array_fill(0, $n, 0);
        $f = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($arr[$i] === 'R') $f = $n;
            elseif ($arr[$i] === 'L') $f = 0;
            else $f = max($f - 1, 0);
            $force[$i] += $f;
        }
        $f = 0;
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($arr[$i] === 'L') $f = $n;
            elseif ($arr[$i] === 'R') $f = 0;
            else $f = max($f - 1, 0);
            $force[$i] -= $f;
        }
        for ($i = 0; $i < $n; $i++) {
            if ($force[$i] > 0) $arr[$i] = 'R';
            elseif ($force[$i] < 0) $arr[$i] = 'L';
            else $arr[$i] = '.';
        }
        return implode('', $arr);
    }
}
