<?php

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function minOperations($n) {
        return intdiv($n * $n, 4);
    }
}
