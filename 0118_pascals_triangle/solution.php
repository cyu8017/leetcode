class Solution {
    function generate($numRows) {
        $result = [];
        for ($rowIndex = 0; $rowIndex < $numRows; $rowIndex++) {
            $row = array_fill(0, $rowIndex + 1, 1);
            for ($index = 1; $index < $rowIndex; $index++) {
                $row[$index] = $result[$rowIndex - 1][$index - 1] + $result[$rowIndex - 1][$index];
            }
            $result[] = $row;
        }
        return $result;
    }
}