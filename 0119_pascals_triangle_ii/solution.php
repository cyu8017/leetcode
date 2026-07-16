class Solution {
    function getRow($rowIndex) {
        $row = [1];
        for ($size = 1; $size <= $rowIndex; $size++) {
            $row[] = 1;
            for ($index = $size - 1; $index >= 1; $index--) {
                $row[$index] += $row[$index - 1];
            }
        }
        return $row;
    }
}