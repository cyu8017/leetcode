<?php
// LeetCode 3709 - Design Exam Scores Tracker
// https://leetcode.com/problems/design-exam-scores-tracker/

class ExamTracker {
    private $times;
    private $pre;

    function __construct() {
        $this->times = [0];
        $this->pre = [0];
    }

    function record($time, $score) {
        $this->times[] = $time;
        $this->pre[] = $this->pre[count($this->pre) - 1] + $score;
    }

    function totalScore($startTime, $endTime) {
        $lowerBound = function($a, $target) {
            $lo = 0;
            $hi = count($a);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($a[$mid] < $target) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };
        $l = $lowerBound($this->times, $startTime) - 1;
        $r = $lowerBound($this->times, $endTime + 1) - 1;
        return $this->pre[$r] - $this->pre[$l];
    }
}
