// LeetCode 0323 - Number of Connected Components in an Undirected Graph
// https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer
     */
    function countComponents($n, $edges) {
        $parent = range(0, $n - 1);
        $rank = array_fill(0, $n, 0);

        $find = function ($node) use (&$find, &$parent) {
            if ($parent[$node] !== $node) {
                $parent[$node] = $find($parent[$node]);
            }
            return $parent[$node];
        };

        $components = $n;
        foreach ($edges as $edge) {
            $rootLeft = $find($edge[0]);
            $rootRight = $find($edge[1]);
            if ($rootLeft === $rootRight) {
                continue;
            }
            if ($rank[$rootLeft] < $rank[$rootRight]) {
                $tmp = $rootLeft;
                $rootLeft = $rootRight;
                $rootRight = $tmp;
            }
            $parent[$rootRight] = $rootLeft;
            if ($rank[$rootLeft] === $rank[$rootRight]) {
                $rank[$rootLeft]++;
            }
            $components--;
        }
        return $components;
    }
}
