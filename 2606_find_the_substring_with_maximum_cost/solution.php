<?php
// LeetCode 2606 - Find the Substring With Maximum Cost
// https://leetcode.com/problems/find-the-substring-with-maximum-cost/

class Solution {
    function maximumCostSubstring($s, $chars, $vals) {
        $val = [];
        for ($i = 0; $i < 26; $i++) $val[$i] = $i + 1;
        $cn = strlen($chars);
        for ($i = 0; $i < $cn; $i++) $val[ord($chars[$i]) - 97] = $vals[$i];
        $best = 0;
        $cur = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $cur += $val[ord($s[$i]) - 97];
            if ($cur < 0) $cur = 0;
            if ($cur > $best) $best = $cur;
        }
        return $best;
    }
}
