<?php
// LeetCode 0552 - Student Attendance Record II
// https://leetcode.com/problems/student-attendance-record-ii/

class Solution {
    function checkRecord($n) {
        $MOD = 1000000007;
        $dp = [[1, 0, 0], [0, 0, 0]];
        for ($day = 0; $day < $n; ++$day) {
            $nxt = [[0, 0, 0], [0, 0, 0]];
            for ($absences = 0; $absences < 2; ++$absences) {
                for ($lates = 0; $lates < 3; ++$lates) {
                    $ways = $dp[$absences][$lates];
                    if ($ways === 0) continue;
                    $nxt[$absences][0] = ($nxt[$absences][0] + $ways) % $MOD;
                    if ($absences === 0) $nxt[1][0] = ($nxt[1][0] + $ways) % $MOD;
                    if ($lates < 2) $nxt[$absences][$lates + 1] = ($nxt[$absences][$lates + 1] + $ways) % $MOD;
                }
            }
            $dp = $nxt;
        }
        $total = 0;
        for ($absences = 0; $absences < 2; ++$absences) {
            for ($lates = 0; $lates < 3; ++$lates) {
                $total = ($total + $dp[$absences][$lates]) % $MOD;
            }
        }
        return $total;
    }
}
