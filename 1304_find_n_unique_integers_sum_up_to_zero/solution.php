<?php
class Solution {
    function sumZero($n) {
        $answer = [];
        for ($value = 1; $value <= intdiv($n, 2); $value++) {
            $answer[] = -$value;
            $answer[] = $value;
        }
        if ($n % 2) $answer[] = 0;
        return $answer;
    }
}
