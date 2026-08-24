<?php
// LeetCode 2704 - To Be Or Not To Be
// https://leetcode.com/problems/to-be-or-not-to-be/

class Solution {
    function expect($val) {
        return [
            'toBe' => function($other) use ($val) {
                if ($val === $other) return true;
                throw new Exception("Not Equal");
            },
            'notToBe' => function($other) use ($val) {
                if ($val !== $other) return true;
                throw new Exception("Equal");
            },
        ];
    }
}
