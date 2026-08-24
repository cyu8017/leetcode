<?php
// LeetCode 2536 - Increment Submatrices by One
// https://leetcode.com/problems/increment-submatrices-by-one/

class Solution {
    function rangeAddQueries($n, $queries) {
        $diff = [];
        for ($i = 0; $i <= $n; $i++) $diff[] = array_fill(0, $n + 1, 0);
        foreach ($queries as $q) {
            $r1 = $q[0]; $c1 = $q[1]; $r2 = $q[2]; $c2 = $q[3];
            $diff[$r1][$c1]++;
            $diff[$r1][$c2 + 1]--;
            $diff[$r2 + 1][$c1]--;
            $diff[$r2 + 1][$c2 + 1]++;
        }
        $mat = [];
        for ($i = 0; $i < $n; $i++) $mat[] = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $v = $diff[$i][$j];
                if ($i > 0) $v += $mat[$i - 1][$j];
                if ($j > 0) $v += $mat[$i][$j - 1];
                if ($i > 0 && $j > 0) $v -= $mat[$i - 1][$j - 1];
                $mat[$i][$j] = $v;
            }
        }
        return $mat;
    }
}
