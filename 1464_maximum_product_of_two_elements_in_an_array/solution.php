<?php
class Solution {
    function maxProduct($nums) {
        sort($nums);
        $n = count($nums);
        return ($nums[$n - 2] - 1) * ($nums[$n - 1] - 1);
    }
}
