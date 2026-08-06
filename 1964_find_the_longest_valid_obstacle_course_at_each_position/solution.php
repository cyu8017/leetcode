<?php
// LeetCode 1964 - Find the Longest Valid Obstacle Course at Each Position
// https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

class Solution {
    /**
     * @param Integer[] $obstacles
     * @return Integer[]
     */
    function longestObstacleCourseAtEachPosition($obstacles) {
        $tails = [];
        $ans = [];
        foreach ($obstacles as $x) {
            $i = $this->bisectRight($tails, $x);
            if ($i === count($tails)) {
                $tails[] = $x;
            } else {
                $tails[$i] = $x;
            }
            $ans[] = $i + 1;
        }
        return $ans;
    }

    private function bisectRight($arr, $x) {
        $lo = 0;
        $hi = count($arr);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($arr[$mid] <= $x) {
                $lo = $mid + 1;
            } else {
                $hi = $mid;
            }
        }
        return $lo;
    }
}
