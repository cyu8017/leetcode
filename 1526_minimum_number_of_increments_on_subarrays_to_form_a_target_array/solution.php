<?php

class Solution {
    /**
     * @param Integer[] $target
     * @return Integer
     */
    function minNumberOperations($target) {
        $answer = $target[0];
        for ($i = 1; $i < count($target); $i++) {
            $answer += max(0, $target[$i] - $target[$i - 1]);
        }
        return $answer;
    }
}
