class Solution {
    func generate(_ numRows: Int) -> [[Int]] {
        var result = [[Int]]()
        for rowIndex in 0..<numRows {
            var row = Array(repeating: 1, count: rowIndex + 1)
            if rowIndex > 1 {
                for index in 1..<rowIndex {
                    row[index] = result[rowIndex - 1][index - 1] + result[rowIndex - 1][index]
                }
            }
            result.append(row)
        }
        return result
    }
}