// LeetCode 0223 - Rectangle Area
// https://leetcode.com/problems/rectangle-area/

class Solution {
    /**
     * @param Integer $ax1
     * @param Integer $ay1
     * @param Integer $ax2
     * @param Integer $ay2
     * @param Integer $bx1
     * @param Integer $by1
     * @param Integer $bx2
     * @param Integer $by2
     * @return Integer
     */
    function computeArea($ax1, $ay1, $ax2, $ay2, $bx1, $by1, $bx2, $by2) {
        $areaA = ($ax2 - $ax1) * ($ay2 - $ay1);
        $areaB = ($bx2 - $bx1) * ($by2 - $by1);
        $overlapW = max(0, min($ax2, $bx2) - max($ax1, $bx1));
        $overlapH = max(0, min($ay2, $by2) - max($ay1, $by1));
        return $areaA + $areaB - $overlapW * $overlapH;
    }
}
