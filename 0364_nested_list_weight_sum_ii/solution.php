// LeetCode 0364 - Nested List Weight Sum II
// https://leetcode.com/problems/nested-list-weight-sum-ii/

class NestedInteger {
    private $integer = null;
    private $list = [];

    function __construct($value = null) {
        if (is_int($value)) {
            $this->integer = $value;
        }
    }

    function isInteger() {
        return $this->integer !== null;
    }

    function getInteger() {
        return $this->integer ?? 0;
    }

    function getList() {
        return $this->list;
    }

    function add($item) {
        $this->list[] = $item;
    }
}

class Solution {
    /**
     * @param NestedInteger[] $nestedList
     * @return Integer
     */
    function depthSum($nestedList) {
        return $this->depth_sum($nestedList);
    }

    /**
     * @param NestedInteger[]|array[] $nestedList
     * @return Integer
     */
    function depth_sum($nestedList) {
        if (!empty($nestedList) && !($nestedList[0] instanceof NestedInteger)) {
            $nestedList = $this->jsonToNestedList($nestedList);
        }

        $weighted = [];
        $dfs = function ($items, $depth) use (&$dfs, &$weighted) {
            foreach ($items as $item) {
                if ($item->isInteger()) {
                    $weighted[] = [$item->getInteger(), $depth];
                } else {
                    $dfs($item->getList(), $depth + 1);
                }
            }
        };

        $dfs($nestedList, 1);
        if (count($weighted) === 0) {
            return 0;
        }

        $maxDepth = max(array_column($weighted, 1));
        $total = 0;
        foreach ($weighted as [$value, $depth]) {
            $total += $value * ($maxDepth - $depth + 1);
        }
        return $total;
    }

    private function jsonToNestedInteger($value) {
        if (is_int($value)) {
            return new NestedInteger($value);
        }

        $item = new NestedInteger();
        foreach ($value as $entry) {
            $item->add($this->jsonToNestedInteger($entry));
        }
        return $item;
    }

    private function jsonToNestedList($values) {
        $result = [];
        foreach ($values as $value) {
            $result[] = $this->jsonToNestedInteger($value);
        }
        return $result;
    }
}
