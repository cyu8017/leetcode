<?php
// LeetCode 0726 - Number of Atoms
// https://leetcode.com/problems/number-of-atoms/

class Solution {
    function countOfAtoms($formula) {
        $st = [[]];
        $i = 0;
        $n = strlen($formula);
        while ($i < $n) {
            if ($formula[$i] === '(') {
                $st[] = [];
                $i++;
            } else if ($formula[$i] === ')') {
                $i++;
                $start = $i;
                while ($i < $n && $formula[$i] >= '0' && $formula[$i] <= '9') $i++;
                $mult = $start < $i ? intval(substr($formula, $start, $i - $start), 10) : 1;
                $top = array_pop($st);
                $peekIdx = count($st) - 1;
                foreach ($top as $key => $value) {
                    $st[$peekIdx][$key] = ($st[$peekIdx][$key] ?? 0) + $value * $mult;
                }
            } else {
                $start = $i++;
                while ($i < $n && $formula[$i] >= 'a' && $formula[$i] <= 'z') $i++;
                $atom = substr($formula, $start, $i - $start);
                $start = $i;
                while ($i < $n && $formula[$i] >= '0' && $formula[$i] <= '9') $i++;
                $count = $start < $i ? intval(substr($formula, $start, $i - $start), 10) : 1;
                $peekIdx = count($st) - 1;
                $st[$peekIdx][$atom] = ($st[$peekIdx][$atom] ?? 0) + $count;
            }
        }
        $peek = $st[count($st) - 1];
        $keys = array_keys($peek);
        sort($keys);
        $result = '';
        foreach ($keys as $key) {
            $result .= $key;
            if ($peek[$key] > 1) $result .= $peek[$key];
        }
        return $result;
    }
}
