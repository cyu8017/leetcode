<?php
class Solution {
    function minimumTotal($triangle) {
        $dp = $triangle[count($triangle) - 1];
        for ($rowIndex = count($triangle) - 2; $rowIndex >= 0; $rowIndex--) {
            foreach ($triangle[$rowIndex] as $index => $value) {
                $dp[$index] = $value + min($dp[$index], $dp[$index + 1]);
            }
        }
        return $dp[0];
    }
}
