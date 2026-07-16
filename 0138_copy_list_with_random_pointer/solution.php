<?php

class Node {
    public $val;
    public $next;
    public $random;

    function __construct($x) {
        $this->val = $x;
        $this->next = null;
        $this->random = null;
    }
}

class Solution {
    function copyRandomList($head) {
        $clones = [];

        $clone = function ($node) use (&$clone, &$clones) {
            if ($node === null) {
                return null;
            }
            $key = spl_object_id($node);
            if (isset($clones[$key])) {
                return $clones[$key];
            }

            $copy = new Node($node->val);
            $clones[$key] = $copy;
            $copy->next = $clone($node->next);
            $copy->random = $clone($node->random);
            return $copy;
        };

        return $clone($head);
    }
}