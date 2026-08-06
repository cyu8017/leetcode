<?php
class Solution {
    function average($salary) {
        return (array_sum($salary) - min($salary) - max($salary)) / (count($salary) - 2);
    }
}
