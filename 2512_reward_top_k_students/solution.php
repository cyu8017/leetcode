<?php
// LeetCode 2512 - Reward Top K Students
// https://leetcode.com/problems/reward-top-k-students/

class Solution {
    function topStudents($positive_feedback, $negative_feedback, $report, $student_id, $k) {
        $pos = [];
        foreach ($positive_feedback as $w) $pos[$w] = true;
        $neg = [];
        foreach ($negative_feedback as $w) $neg[$w] = true;
        $arr = [];
        for ($i = 0; $i < count($report); $i++) {
            $score = 0;
            foreach (explode(' ', $report[$i]) as $w) {
                if ($w === '') continue;
                if (isset($pos[$w])) $score += 3;
                elseif (isset($neg[$w])) $score--;
            }
            $arr[] = [$student_id[$i], $score];
        }
        usort($arr, function ($a, $b) {
            if ($a[1] !== $b[1]) return $b[1] <=> $a[1];
            return $a[0] <=> $b[0];
        });
        $ans = [];
        for ($i = 0; $i < $k; $i++) $ans[] = $arr[$i][0];
        return $ans;
    }
}
