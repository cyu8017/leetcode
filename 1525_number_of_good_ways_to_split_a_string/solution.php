<?php

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function numSplits($s) {
        $right = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            $right[$ch] = ($right[$ch] ?? 0) + 1;
        }
        $left = [];
        $answer = 0;
        for ($i = 0; $i < $n - 1; $i++) {
            $ch = $s[$i];
            $left[$ch] = true;
            $right[$ch]--;
            if ($right[$ch] === 0) {
                unset($right[$ch]);
            }
            if (count($left) === count($right)) {
                $answer++;
            }
        }
        return $answer;
    }
}
