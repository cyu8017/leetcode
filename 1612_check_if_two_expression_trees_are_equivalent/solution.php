<?php
// LeetCode 1612 - Check If Two Expression Trees are Equivalent
// https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/

class Node {
    public $val;
    public $left = null;
    public $right = null;

    function __construct($val = "") {
        $this->val = $val;
    }
}

class Solution {
    private function parse($data) {
        if (!is_string($data)) {
            return $data;
        }
        $inner = trim($data, "[]");
        $vals = $inner === "" ? [] : explode(",", $inner);
        $nodes = [];
        foreach ($vals as $x) {
            $nodes[] = $x === "null" ? null : new Node($x);
        }
        $idx = 1;
        $n = count($nodes);
        for ($i = 0; $i < $n; $i++) {
            if ($nodes[$i] !== null) {
                $nodes[$i]->left = $idx < $n ? $nodes[$idx++] : null;
                $nodes[$i]->right = $idx < $n ? $nodes[$idx++] : null;
            }
        }
        return $nodes ? $nodes[0] : null;
    }

    private function countFreq($node, &$out) {
        if ($node === null) {
            return;
        }
        if ($node->val === "+") {
            $this->countFreq($node->left, $out);
            $this->countFreq($node->right, $out);
        } else {
            $out[$node->val] = ($out[$node->val] ?? 0) + 1;
        }
    }

    /**
     * @param Node|String $root1
     * @param Node|String $root2
     * @return Boolean
     */
    function checkEquivalence($root1, $root2) {
        $a = [];
        $b = [];
        $this->countFreq($this->parse($root1), $a);
        $this->countFreq($this->parse($root2), $b);
        ksort($a);
        ksort($b);
        return $a === $b;
    }
}
