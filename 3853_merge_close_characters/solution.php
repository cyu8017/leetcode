<?php
// LeetCode 3853 - Merge Close Characters
// https://leetcode.com/problems/merge-close-characters/

class Solution {
    function mergeCharacters($s, $k) {
        $last = [];
        $ans = '';
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            $cur = strlen($ans);
            if (isset($last[$c]) && $cur - $last[$c] <= $k) continue;
            $ans .= $c;
            $last[$c] = $cur;
        }
        return $ans;
    }
}
