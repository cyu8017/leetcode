<?php

class Solution {
    /**
     * @param Integer $low
     * @param Integer $high
     * @return Integer
     */
    function countOdds($low, $high) {
        return intdiv($high + 1, 2) - intdiv($low, 2);
    }
}
