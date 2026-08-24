<?php
// LeetCode 2830 - Maximize the Profit as the Salesman
// https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

class Solution {
    function maximizeTheProfit($n, $offers) {
        $byEnd = array_fill(0, $n, []);
        foreach ($offers as $o) $byEnd[$o[1]][] = $o;
        $dp = array_fill(0, $n + 1, 0);
        for ($end = 0; $end < $n; $end++) {
            $dp[$end + 1] = $dp[$end];
            foreach ($byEnd[$end] as $o)
                $dp[$end + 1] = max($dp[$end + 1], $dp[$o[0]] + $o[2]);
        }
        return $dp[$n];
    }
}
