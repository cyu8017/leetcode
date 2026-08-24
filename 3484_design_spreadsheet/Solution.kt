// LeetCode 3484 - Design Spreadsheet
// https://leetcode.com/problems/design-spreadsheet/

class Spreadsheet(rows: Int) {
    private val cells = HashMap<String, Int>()

    fun setCell(cell: String, value: Int) {
        cells[cell] = value
    }

    fun resetCell(cell: String) {
        cells.remove(cell)
    }

    fun getValue(formula: String): Int {
        var f = formula
        if (f.isNotEmpty() && f[0] == '=') f = f.substring(1)
        var sum = 0
        var start = 0
        while (start < f.length) {
            val plus = f.indexOf('+', start)
            val p = if (plus < 0) f.substring(start) else f.substring(start, plus)
            var isNum = p.isNotEmpty() && (p[0].isDigit() || (p[0] == '-' && p.length > 1))
            if (isNum) {
                for (i in 1 until p.length) {
                    if (!p[i].isDigit()) {
                        isNum = false
                        break
                    }
                }
            }
            sum += if (isNum) p.toInt() else cells.getOrDefault(p, 0)
            if (plus < 0) break
            start = plus + 1
        }
        return sum
    }
}
