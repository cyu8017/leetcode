<?php
// LeetCode 3662 - Filter Characters by Frequency
// https://leetcode.com/problems/filter-characters-by-frequency/

class Solution {
    function filterCharacters($s, $k) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        $ans = '';
        for ($i = 0; $i < $n; $i++)
            if ($cnt[ord($s[$i]) - 97] < $k) $ans .= $s[$i];
        return $ans;
    }
}
