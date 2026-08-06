<?php

class Node {
    public $val = null;
    /** @var Node[] */
    public $children = [];

    function __construct($val = null, $children = null) {
        $this->val = $val;
        $this->children = $children ?? [];
    }
}

class Solution {
    /**
     * @param Node|null $root
     * @return Integer
     */
    function diameter($root) {
        $answer = 0;
        $depth = function ($node) use (&$depth, &$answer) {
            $longest = 0;
            $second = 0;
            foreach ($node->children as $child) {
                $value = $depth($child) + 1;
                if ($value > $longest) {
                    $second = $longest;
                    $longest = $value;
                } elseif ($value > $second) {
                    $second = $value;
                }
            }
            $answer = max($answer, $longest + $second);
            return $longest;
        };
        if ($root !== null) {
            $depth($root);
        }
        return $answer;
    }
}
