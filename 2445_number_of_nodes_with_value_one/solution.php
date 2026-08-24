<?php
// LeetCode 2445 - Number of Nodes With Value One
// https://leetcode.com/problems/number-of-nodes-with-value-one/

class Solution {
    function numberOfNodes($n, $queries) {
        $flip = array_fill(0, $n + 1, 0);
        $val = array_fill(0, $n + 1, 0);
        foreach ($queries as $q) $flip[$q] ^= 1;
        $ans = 0;
        for ($i = 1; $i <= $n; $i++) {
            $val[$i] = $flip[$i];
            if ($i > 1) $val[$i] ^= $val[intdiv($i, 2)];
            $ans += $val[$i];
        }
        return $ans;
    }
}
