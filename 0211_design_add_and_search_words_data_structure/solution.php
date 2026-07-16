// LeetCode 0211 - Design Add and Search Words Data Structure
// https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode {
    public $children = [];
    public $isWord = false;
}

class WordDictionary {
    private $root;

    function __construct() {
        $this->root = new TrieNode();
    }

    function addWord($word) {
        $node = $this->root;
        for ($i = 0; $i < strlen($word); $i++) {
            $char = $word[$i];
            if (!isset($node->children[$char])) {
                $node->children[$char] = new TrieNode();
            }
            $node = $node->children[$char];
        }
        $node->isWord = true;
    }

    function search($word) {
        return $this->dfs($this->root, $word, 0);
    }

    private function dfs($node, $word, $index) {
        if ($index === strlen($word)) {
            return $node->isWord;
        }
        $char = $word[$index];
        if ($char === '.') {
            foreach ($node->children as $child) {
                if ($this->dfs($child, $word, $index + 1)) {
                    return true;
                }
            }
            return false;
        }
        if (!isset($node->children[$char])) {
            return false;
        }
        return $this->dfs($node->children[$char], $word, $index + 1);
    }
}
