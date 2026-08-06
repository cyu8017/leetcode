<?php

class Solution {
    /**
     * @param String $s
     * @param Integer[] $indices
     * @return String
     */
    function restoreString($s, $indices) {
        $answer = array_fill(0, strlen($s), '');
        for ($i = 0; $i < strlen($s); $i++) {
            $answer[$indices[$i]] = $s[$i];
        }
        return implode('', $answer);
    }
}
