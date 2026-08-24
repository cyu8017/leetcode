<?php
// LeetCode 0551 - Student Attendance Record I
// https://leetcode.com/problems/student-attendance-record-i/

class Solution {
    function checkRecord($s) {
        $absents = 0;
        $lateStreak = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if ($ch === "A") {
                ++$absents;
                if ($absents >= 2) return false;
                $lateStreak = 0;
            } elseif ($ch === "L") {
                ++$lateStreak;
                if ($lateStreak >= 3) return false;
            } else {
                $lateStreak = 0;
            }
        }
        return true;
    }
}
