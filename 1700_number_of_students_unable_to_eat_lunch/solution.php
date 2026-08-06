<?php
// LeetCode 1700 - Number of Students Unable to Eat Lunch
// https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution {
    function countStudents($students, $sandwiches) {
        $c = array_count_values($students);
        $n = count($students);
        foreach ($sandwiches as $i => $x) {
            if (empty($c[$x])) {
                return $n - $i;
            }
            $c[$x]--;
        }
        return 0;
    }
}
