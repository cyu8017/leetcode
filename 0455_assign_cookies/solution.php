// LeetCode 0455 - Assign Cookies
// https://leetcode.com/problems/assign-cookies/

class Solution {
    /**
     * @param int[] $g
     * @param int[] $s
     * @return int
     */
    function findContentChildren($g, $s) {
        return $this->find_content_children($g, $s);
    }

    /**
     * @param int[] $g
     * @param int[] $s
     * @return int
     */
    function find_content_children($g, $s) {
        sort($g);
        sort($s);
        $child = 0;
        $cookie = 0;
        while ($child < count($g) && $cookie < count($s)) {
            if ($s[$cookie] >= $g[$child]) {
                $child++;
            }
            $cookie++;
        }
        return $child;
    }
}
