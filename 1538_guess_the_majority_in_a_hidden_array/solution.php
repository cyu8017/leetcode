<?php

class ArrayReader {
    private $nums;

    function __construct($nums) {
        $this->nums = $nums;
    }

    function query($a, $b, $c, $d) {
        $ones = $this->nums[$a] + $this->nums[$b] + $this->nums[$c] + $this->nums[$d];
        if ($ones === 0 || $ones === 4) {
            return 4;
        }
        if ($ones === 1 || $ones === 3) {
            return 2;
        }
        return 0;
    }

    function length() {
        return count($this->nums);
    }
}

class Solution {
    /**
     * @param Integer[]|ArrayReader $reader
     * @return Integer
     */
    function guessMajority($reader) {
        if (is_array($reader)) {
            $reader = new ArrayReader($reader);
        }
        $n = $reader->length();
        $firstFour = $reader->query(0, 1, 2, 3);
        $shifted = $reader->query(1, 2, 3, 4);
        $same = 1;
        $different = 0;
        $differentIndex = -1;
        $laterDifferent = -1;
        $fourSame = $firstFour === $shifted;
        if ($fourSame) {
            $same++;
        } else {
            $different++;
            $differentIndex = 4;
        }
        $checks = [[0, 2, 3, 4], [0, 1, 3, 4], [0, 1, 2, 4]];
        foreach ($checks as $index => $args) {
            if ($reader->query($args[0], $args[1], $args[2], $args[3]) === $shifted) {
                $same++;
            } else {
                $different++;
                $differentIndex = $index + 1;
            }
        }
        for ($i = 5; $i < $n; $i++) {
            $iSameAsFour = $reader->query(1, 2, 3, $i) === $shifted;
            if ($iSameAsFour === $fourSame) {
                $same++;
            } else {
                $different++;
                $differentIndex = $i;
                if ($laterDifferent === -1) {
                    $laterDifferent = $i;
                }
            }
        }
        if ($same === $different) {
            return -1;
        }
        return $same > $different ? 0 : ($laterDifferent !== -1 ? $laterDifferent : $differentIndex);
    }
}
