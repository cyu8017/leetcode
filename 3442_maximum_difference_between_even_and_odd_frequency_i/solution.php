<?php
// LeetCode 3442 - Maximum Difference Between Even and Odd Frequency I
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

class Solution {
    function maxDifference($s) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $freq[ord($s[$i]) - 97]++;
        $maxOdd = 0;
        $minEven = 1e9;
        foreach ($freq as $f) {
            if ($f === 0) continue;
            if ($f % 2 === 1) {
                if ($f > $maxOdd) $maxOdd = $f;
            } else if ($f < $minEven) $minEven = $f;
        }
        return $maxOdd - $minEven;
    }
}
