<?php
// LeetCode 2067 - Number of Equal Count Substrings
// https://leetcode.com/problems/number-of-equal-count-substrings/

class Solution {
    /**
     * @param String $s
     * @param Integer $count
     * @return Integer
     */
    function equalCountSubstrings($s, $count) {
        $ans = 0;
        $n = strlen($s);
        $seen = array_fill(0, 26, false);
        $maxUnique = 0;
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 97;
            if (!$seen[$idx]) { $seen[$idx] = true; $maxUnique++; }
        }
        for ($u = 1; $u <= $maxUnique; $u++) {
            $needLen = $u * $count;
            if ($needLen > $n) break;
            $freq = array_fill(0, 26, 0);
            $have = 0;
            for ($i = 0; $i < $n; $i++) {
                $c = ord($s[$i]) - 97;
                $freq[$c]++;
                if ($freq[$c] === $count) $have++;
                else if ($freq[$c] === $count + 1) $have--;
                if ($i >= $needLen) {
                    $p = ord($s[$i - $needLen]) - 97;
                    if ($freq[$p] === $count) $have--;
                    else if ($freq[$p] === $count + 1) $have++;
                    $freq[$p]--;
                }
                if ($i + 1 >= $needLen && $have === $u) $ans++;
            }
        }
        return $ans;
    }
}
