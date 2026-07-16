<?php

class Solution {
    function singleNumber($nums) {
        $result = 0;
        foreach ($nums as $num) {
            $result ^= $num;
        }
        return $result;
    }
}