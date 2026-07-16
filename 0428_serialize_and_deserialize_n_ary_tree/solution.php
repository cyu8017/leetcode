// LeetCode 0428 - Serialize and Deserialize N-ary Tree
// https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

class Node {
    public $val = null;
    /** @var Node[] */
    public $children = [];
    function __construct($val = null, $children = null) {
        $this->val = $val;
        $this->children = $children ?? [];
    }
}

class Codec {
    /**
     * @param Node|null $root
     * @return String
     */
    function encode($root) {
        if ($root === null) {
            return "";
        }

        $parts = [];
        $queue = [$root];
        while (count($queue) > 0) {
            $node = array_shift($queue);
            $parts[] = (string)$node->val;
            $parts[] = (string)count($node->children);
            foreach ($node->children as $child) {
                $parts[] = (string)$child->val;
                $queue[] = $child;
            }
        }
        return implode(",", $parts);
    }

    /**
     * @param String $data
     * @return Node|null
     */
    function decode($data) {
        if ($data === "") {
            return null;
        }

        $values = explode(",", $data);
        $index = 0;

        $value = (int)$values[$index];
        $childCount = (int)$values[$index + 1];
        $index += 2;
        $root = new Node($value, []);
        for ($i = 0; $i < $childCount; $i++) {
            $root->children[] = new Node((int)$values[$index], []);
            $index++;
        }

        $queue = $root->children;
        while (count($queue) > 0) {
            $node = array_shift($queue);
            $childCount = (int)$values[$index + 1];
            $index += 2;
            for ($i = 0; $i < $childCount; $i++) {
                $child = new Node((int)$values[$index], []);
                $node->children[] = $child;
                $queue[] = $child;
                $index++;
            }
        }

        return $root;
    }

    function serialize($root) {
        return $this->encode($root);
    }

    function deserialize($data) {
        return $this->decode($data);
    }
}
