<?php
class Solution {
    function smallerNumbersThanCurrent($nums) {
        $sorted = $nums;
        sort($sorted);
        $rank = [];
        foreach ($sorted as $i => $x) {
            if (!array_key_exists($x, $rank)) $rank[$x] = $i;
        }
        $answer = [];
        foreach ($nums as $x) $answer[] = $rank[$x];
        return $answer;
    }
}
