<?php
class Solution {
    /**
     * @param Integer[] $rungs
     * @param Integer $dist
     * @return Integer
     */
    function addRungs($rungs, $dist) {
        $prev = 0;
        $ans = 0;
        foreach ($rungs as $r) {
            $gap = $r - $prev;
            if ($gap > $dist) {
                $ans += intdiv($gap - 1, $dist);
            }
            $prev = $r;
        }
        return $ans;
    }
}
