<?php
// LeetCode 0997 - Find the Town Judge
// https://leetcode.com/problems/find-the-town-judge/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $trust
     * @return Integer
     */
    function findJudge($n, $trust) {
        $score = array_fill(0, $n + 1, 0);
        foreach ($trust as $t) {
            $score[$t[0]]--;
            $score[$t[1]]++;
        }
        for ($i = 1; $i <= $n; $i++) if ($score[$i] === $n - 1) return $i;
        return -1;
    }
}
