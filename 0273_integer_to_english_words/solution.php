<?php
// LeetCode 0273 - Integer to English Words
// https://leetcode.com/problems/integer-to-english-words/

class Solution {
    private $ones = [
        "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
        "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
        "Seventeen", "Eighteen", "Nineteen",
    ];
    private $tens = [
        "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety",
    ];
    private $thousands = ["", "Thousand", "Million", "Billion"];

    /**
     * @param Integer $num
     * @return String
     */
    function numberToWords($num) {
        if ($num === 0) {
            return "Zero";
        }

        $parts = [];
        $chunkIndex = 0;
        while ($num > 0) {
            $chunk = $num % 1000;
            if ($chunk !== 0) {
                $chunkWords = $this->convertChunk($chunk);
                if ($this->thousands[$chunkIndex] !== "") {
                    $chunkWords .= " " . $this->thousands[$chunkIndex];
                }
                $parts[] = $chunkWords;
            }
            $num = intdiv($num, 1000);
            $chunkIndex++;
        }
        return implode(" ", array_reverse($parts));
    }

    private function convertChunk($value) {
        if ($value === 0) {
            return "";
        }
        if ($value < 20) {
            return $this->ones[$value];
        }
        if ($value < 100) {
            $tensPart = $this->tens[intdiv($value, 10)];
            $onesPart = $this->ones[$value % 10];
            return $onesPart === "" ? $tensPart : "$tensPart $onesPart";
        }
        $hundreds = $this->ones[intdiv($value, 100)];
        $remainder = $this->convertChunk($value % 100);
        return $remainder === "" ? "$hundreds Hundred" : "$hundreds Hundred $remainder";
    }
}
