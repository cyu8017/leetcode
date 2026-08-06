<?php

class Solution {
    /**
     * @param String $target
     * @return Integer
     */
    function minFlips($target) {
        $answer = 0;
        $prev = '0';
        $n = strlen($target);
        for ($i = 0; $i < $n; $i++) {
            if ($prev !== $target[$i]) {
                $answer++;
            }
            $prev = $target[$i];
        }
        return $answer;
    }
}
