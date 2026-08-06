<?php
class Solution {
    function runningSum($nums) {
        for ($i = 1; $i < count($nums); $i++) $nums[$i] += $nums[$i - 1];
        return $nums;
    }
}
