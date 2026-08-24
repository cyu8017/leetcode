<?php
// LeetCode 2162 - Minimum Cost to Set Cooking Time
// https://leetcode.com/problems/minimum-cost-to-set-cooking-time/

class Solution {
    private function cost($mins, $secs, $startAt, $moveCost, $pushCost) {
        if ($mins < 0 || $mins > 99 || $secs < 0 || $secs > 99) return PHP_INT_MAX >> 2;
        if ($mins > 0) $s = (string)$mins . (string)intdiv($secs, 10) . (string)($secs % 10);
        else $s = (string)$secs;
        $cur = (string)$startAt;
        $ans = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if ($c !== $cur) { $ans += $moveCost; $cur = $c; }
            $ans += $pushCost;
        }
        return $ans;
    }

    /**
     * @param Integer $startAt
     * @param Integer $moveCost
     * @param Integer $pushCost
     * @param Integer $targetSeconds
     * @return Integer
     */
    function minCostSetTime($startAt, $moveCost, $pushCost, $targetSeconds) {
        $mins = intdiv($targetSeconds, 60);
        $secs = $targetSeconds % 60;
        $ans = $this->cost($mins, $secs, $startAt, $moveCost, $pushCost);
        if ($mins > 0) $ans = min($ans, $this->cost($mins - 1, $secs + 60, $startAt, $moveCost, $pushCost));
        return $ans;
    }
}
