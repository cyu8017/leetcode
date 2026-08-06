<?php

class TreeNode {
    public $val;
    public $left;
    public $right;

    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class BSTIterator {
    private $values = [];
    private $index = -1;

    /**
     * @param TreeNode $root
     */
    function __construct($root) {
        $stack = [];
        while (!empty($stack) || $root !== null) {
            while ($root !== null) {
                $stack[] = $root;
                $root = $root->left;
            }
            $root = array_pop($stack);
            $this->values[] = $root->val;
            $root = $root->right;
        }
    }

    /**
     * @return Boolean
     */
    function hasNext() {
        return $this->index + 1 < count($this->values);
    }

    /**
     * @return Integer
     */
    function next() {
        $this->index++;
        return $this->values[$this->index];
    }

    /**
     * @return Boolean
     */
    function hasPrev() {
        return $this->index > 0;
    }

    /**
     * @return Integer
     */
    function prev() {
        $this->index--;
        return $this->values[$this->index];
    }
}
