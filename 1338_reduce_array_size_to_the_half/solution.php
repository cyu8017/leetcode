<?php
class Solution {
    function minSetSize($arr) {
        $counts = array_count_values($arr);
        rsort($counts);
        $removed = 0;
        $need = intdiv(count($arr), 2);
        $answer = 0;
        foreach ($counts as $c) {
            $removed += $c;
            $answer++;
            if ($removed >= $need) return $answer;
        }
        return $answer;
    }
}
