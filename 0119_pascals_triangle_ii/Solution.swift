class Solution {
    func getRow(_ rowIndex: Int) -> [Int] {
        var row = [1]
        if rowIndex == 0 { return row }
        for size in 1...rowIndex {
            row.append(1)
            if size > 1 {
                for index in stride(from: size - 1, through: 1, by: -1) {
                    row[index] += row[index - 1]
                }
            }
        }
        return row
    }
}