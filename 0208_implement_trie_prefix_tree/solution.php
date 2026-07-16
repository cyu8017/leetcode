// LeetCode 0208 - Implement Trie (Prefix Tree)
// https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode {
    public $children = [];
    public $isWord = false;
}

class Trie {
    private $root;

    function __construct() {
        $this->root = new TrieNode();
    }

    function insert($word) {
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
        $node = $this->find($word);
        return $node !== null && $node->isWord;
    }

    function startsWith($prefix) {
        return $this->find($prefix) !== null;
    }

    private function find($text) {
        $node = $this->root;
        for ($i = 0; $i < strlen($text); $i++) {
            $char = $text[$i];
            if (!isset($node->children[$char])) {
                return null;
            }
            $node = $node->children[$char];
        }
        return $node;
    }
}