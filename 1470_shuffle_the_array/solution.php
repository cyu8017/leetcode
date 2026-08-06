<?php
class Solution {
    function shuffle($nums, $n) {
        $answer = [];
        for ($i = 0; $i < $n; $i++) {
            $answer[] = $nums[$i];
            $answer[] = $nums[$i + $n];
        }
        return $answer;
    }
}
