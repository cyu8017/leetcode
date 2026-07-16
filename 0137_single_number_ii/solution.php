<?php

class Solution {
    function singleNumber($nums) {
        $ones = 0;
        $twos = 0;
        foreach ($nums as $num) {
            $ones = ($ones ^ $num) & ~$twos;
            $twos = ($twos ^ $num) & ~$ones;
        }
        return $ones;
    }
}