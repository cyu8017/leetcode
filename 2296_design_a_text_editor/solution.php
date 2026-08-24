<?php
// LeetCode 2296 - Design a Text Editor
// https://leetcode.com/problems/design-a-text-editor/

class TextEditor {
    private $left = [];
    private $right = [];

    function __construct() {
        $this->left = [];
        $this->right = [];
    }

    private function suffix() {
        $start = max(0, count($this->left) - 10);
        return implode('', array_slice($this->left, $start));
    }

    function addText($text) {
        $n = strlen($text);
        for ($i = 0; $i < $n; $i++) $this->left[] = $text[$i];
    }

    function deleteText($k) {
        $deleted = 0;
        while ($k > 0 && count($this->left)) {
            array_pop($this->left);
            $k--;
            $deleted++;
        }
        return $deleted;
    }

    function cursorLeft($k) {
        while ($k > 0 && count($this->left)) {
            $this->right[] = array_pop($this->left);
            $k--;
        }
        return $this->suffix();
    }

    function cursorRight($k) {
        while ($k > 0 && count($this->right)) {
            $this->left[] = array_pop($this->right);
            $k--;
        }
        return $this->suffix();
    }
}
