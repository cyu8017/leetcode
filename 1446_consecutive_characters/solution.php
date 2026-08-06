<?php
class Solution {
    function maxPower($s) {
        $answer = 1;
        $run = 1;
        for ($i = 1; $i < strlen($s); $i++) {
            $run = $s[$i] === $s[$i - 1] ? $run + 1 : 1;
            $answer = max($answer, $run);
        }
        return $answer;
    }
}
