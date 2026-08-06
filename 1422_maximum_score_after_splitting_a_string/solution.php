<?php
class Solution {
    function maxScore($s) {
        $ones = substr_count($s, "1");
        $leftZeros = 0;
        $answer = 0;
        for ($i = 0; $i < strlen($s) - 1; $i++) {
            if ($s[$i] === "0") $leftZeros++;
            else $ones--;
            $answer = max($answer, $leftZeros + $ones);
        }
        return $answer;
    }
}
