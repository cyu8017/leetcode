<?php
// LeetCode 2545 - Sort the Students by Their Kth Score
// https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution {
    function sortTheStudents($score, $k) {
        usort($score, function($a, $b) use ($k) { return $b[$k] <=> $a[$k]; });
        return $score;
    }
}
