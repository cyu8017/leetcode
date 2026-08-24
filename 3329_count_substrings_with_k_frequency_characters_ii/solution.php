<?php
// LeetCode 3329 - Count Substrings With K-Frequency Characters II
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-ii/

class Solution {
    function numberOfSubstrings($s, $k) {
        $n = strlen($s);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $freq = array_fill(0, 26, 0);
            for ($j = $i; $j < $n; $j++) {
                $freq[ord($s[$j]) - 97]++;
                $ok = false;
                foreach ($freq as $f) if ($f >= $k) { $ok = true; break; }
                if ($ok) { $ans += $n - $j; break; }
            }
        }
        return $ans;
    }
}
