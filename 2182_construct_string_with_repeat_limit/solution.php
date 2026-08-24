<?php
// LeetCode 2182 - Construct String With Repeat Limit
// https://leetcode.com/problems/construct-string-with-repeat-limit/

class Solution {
    /**
     * @param String $s
     * @param Integer $repeatLimit
     * @return String
     */
    function repeatLimitedString($s, $repeatLimit) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $freq[ord($s[$i]) - 97]++;
        $ans = [];
        while (true) {
            $placed = false;
            for ($c = 25; $c >= 0; $c--) {
                if ($freq[$c] === 0) continue;
                if ($ans && ord($ans[count($ans) - 1]) - 97 === $c) {
                    $found = false;
                    for ($d = $c - 1; $d >= 0; $d--) {
                        if ($freq[$d] > 0) {
                            $ans[] = chr(97 + $d);
                            $freq[$d]--;
                            $found = true;
                            $placed = true;
                            break;
                        }
                    }
                    if (!$found) return implode('', $ans);
                    break;
                }
                $use = min($freq[$c], $repeatLimit);
                for ($i = 0; $i < $use; $i++) $ans[] = chr(97 + $c);
                $freq[$c] -= $use;
                $placed = true;
                break;
            }
            if (!$placed) break;
        }
        return implode('', $ans);
    }
}
