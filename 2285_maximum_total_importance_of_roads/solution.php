<?php
// LeetCode 2285 - Maximum Total Importance of Roads
// https://leetcode.com/problems/maximum-total-importance-of-roads/

class Solution {
    function maximumImportance($n, $roads) {
        $deg = array_fill(0, $n, 0);
        foreach ($roads as $r) { $deg[$r[0]]++; $deg[$r[1]]++; }
        sort($deg);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) $ans += $deg[$i] * ($i + 1);
        return $ans;
    }
}
