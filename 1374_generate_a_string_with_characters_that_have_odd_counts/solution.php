<?php
class Solution {
    function generateTheString($n) {
        return $n % 2 ? str_repeat("a", $n) : str_repeat("a", $n - 1) . "b";
    }
}
