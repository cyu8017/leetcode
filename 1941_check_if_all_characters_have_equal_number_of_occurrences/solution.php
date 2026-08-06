<?php

class Solution {
    /**
     * @param String $s
     * @return Boolean
     */
    function areOccurrencesEqual($s) {
        $freq = array_count_values(str_split($s));
        return count(array_unique(array_values($freq))) === 1;
    }
}
