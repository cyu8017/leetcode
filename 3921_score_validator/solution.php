<?php
// LeetCode 3921 - Score Validator
// https://leetcode.com/problems/score-validator/

class Solution {
    function scoreValidator($events) {
        $score = 0;
        $counter = 0;
        foreach ($events as $eventStr) {
            $isNum = strlen($eventStr) > 0;
            $num = 0;
            $start = 0;
            if ($isNum && $eventStr[0] === '-') $start = 1;
            $len = strlen($eventStr);
            for ($i = $start; $i < $len; $i++) {
                if ($eventStr[$i] < '0' || $eventStr[$i] > '9') {
                    $isNum = false;
                    break;
                }
                $num = $num * 10 + (ord($eventStr[$i]) - 48);
            }
            if ($isNum && !($start === 1 && $len === 1)) {
                if ($start === 1) $num = -$num;
                $score += $num;
            } else if ($eventStr === 'W') {
                $counter++;
                if ($counter === 10) break;
            } else {
                $score++;
            }
        }
        return [$score, $counter];
    }
}
