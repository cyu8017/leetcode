<?php
// LeetCode 3819 - Rotate Non Negative Elements
// https://leetcode.com/problems/rotate-non-negative-elements/

class Solution {
    function rotateElements($nums, $k) {
        $t = [];
        foreach ($nums as $x) if ($x >= 0) $t[] = $x;
        $m = count($t);
        if ($m === 0) return $nums;
        $d = array_fill(0, $m, 0);
        for ($i = 0; $i < $m; $i++) $d[(($i - $k) % $m + $m) % $m] = $t[$i];
        $j = 0;
        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] >= 0) $nums[$i] = $d[$j++];
        }
        return $nums;
    }
}
