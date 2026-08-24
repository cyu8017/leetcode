<?php
// LeetCode 3084 - Count Substrings Starting and Ending with Given Character
// https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/

class Solution {
    function countSubstrings($s, $c) {
        $cnt = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) if ($s[$i] === $c) $cnt++;
        return intdiv($cnt * ($cnt + 1), 2);
    }
}
