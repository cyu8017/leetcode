<?php
// LeetCode 3388 - Count Beautiful Splits in an Array
// https://leetcode.com/problems/count-beautiful-splits-in-an-array/

class Solution {
    function equal($a, $as, $ae, $b, $bs, $be) {
        if ($ae - $as !== $be - $bs) return false;
        for ($i = 0; $i < $ae - $as; $i++) if ($a[$as + $i] !== $b[$bs + $i]) return false;
        return true;
    }

    function beautifulSplits($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 1; $i < $n - 1; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $ok = false;
                if ($i <= $j - $i && $this->equal($nums, 0, $i, $nums, $i, $i + $i)) $ok = true;
                if (!$ok && $j - $i <= $n - $j && $this->equal($nums, $i, $j, $nums, $j, $j + ($j - $i))) $ok = true;
                if ($ok) $ans++;
            }
        }
        return $ans;
    }
}
