<?php
// LeetCode 3606 - Coupon Code Validator
// https://leetcode.com/problems/coupon-code-validator/

class Solution {
    private function check($s) {
        if ($s === '' || $s === null) return false;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if (!(($c >= 'A' && $c <= 'Z') || ($c >= 'a' && $c <= 'z') || ($c >= '0' && $c <= '9') || $c === '_'))
                return false;
        }
        return true;
    }

    function validateCoupons($code, $businessLine, $isActive) {
        $bs = ['electronics' => 1, 'grocery' => 1, 'pharmacy' => 1, 'restaurant' => 1];
        $idx = [];
        for ($i = 0; $i < count($code); $i++) {
            if ($isActive[$i] && isset($bs[$businessLine[$i]]) && $this->check($code[$i])) $idx[] = $i;
        }
        usort($idx, function($i, $j) use ($businessLine, $code) {
            $c = $businessLine[$i] <=> $businessLine[$j];
            if ($c !== 0) return $c;
            return $code[$i] <=> $code[$j];
        });
        $ans = [];
        foreach ($idx as $i) $ans[] = $code[$i];
        return $ans;
    }
}
