// LeetCode 0168 - Excel Sheet Column Title
// https://leetcode.com/problems/excel-sheet-column-title/

class Solution {
    function convertToTitle(int $columnNumber): string {
        $chars = [];
        while ($columnNumber > 0) {
            $columnNumber--;
            $chars[] = chr(ord("A") + $columnNumber % 26);
            $columnNumber = intdiv($columnNumber, 26);
        }
        return implode("", array_reverse($chars));
    }
}