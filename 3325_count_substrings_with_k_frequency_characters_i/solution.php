<?php
// LeetCode 3325 - Count Substrings With K-Frequency Characters I
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/

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
