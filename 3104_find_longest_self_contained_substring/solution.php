<?php
// LeetCode 3104 - Find Longest Self-Contained Substring
// https://leetcode.com/problems/find-longest-self-contained-substring/

class Solution {
    function maxSubstringLength($s) {
        $first = array_fill(0, 26, -1);
        $last = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $j = ord($s[$i]) - 97;
            if ($first[$j] === -1) $first[$j] = $i;
            $last[$j] = $i;
        }
        $ans = -1;
        for ($k = 0; $k < 26; $k++) {
            $i = $first[$k];
            if ($i === -1) continue;
            $mx = $last[$k];
            for ($j = $i; $j < $n; $j++) {
                $a = $first[ord($s[$j]) - 97];
                $b = $last[ord($s[$j]) - 97];
                if ($a < $i) break;
                $mx = max($mx, $b);
                if ($mx === $j && $j - $i + 1 < $n) $ans = max($ans, $j - $i + 1);
            }
        }
        return $ans;
    }
}
