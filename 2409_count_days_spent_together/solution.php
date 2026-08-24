<?php
// LeetCode 2409 - Count Days Spent Together
// https://leetcode.com/problems/count-days-spent-together/

class Solution {
    function countDaysTogether($arriveAlice, $leaveAlice, $arriveBob, $leaveBob) {
        $a1 = $this->toDay($arriveAlice);
        $a2 = $this->toDay($leaveAlice);
        $b1 = $this->toDay($arriveBob);
        $b2 = $this->toDay($leaveBob);
        $start = max($a1, $b1);
        $end = min($a2, $b2);
        if ($end < $start) return 0;
        return $end - $start + 1;
    }

    private function toDay($s) {
        $DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        $m = (ord($s[0]) - 48) * 10 + (ord($s[1]) - 48);
        $d = (ord($s[3]) - 48) * 10 + (ord($s[4]) - 48);
        $res = $d;
        for ($i = 0; $i < $m - 1; $i++) $res += $DAYS[$i];
        return $res;
    }
}
