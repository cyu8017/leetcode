<?php
class Solution {
    function maxSatisfaction($satisfaction) {
        rsort($satisfaction);
        $total = 0;
        $answer = 0;
        foreach ($satisfaction as $value) {
            if ($total + $value <= 0) break;
            $total += $value;
            $answer += $total;
        }
        return $answer;
    }
}
