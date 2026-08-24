// LeetCode 0631 - Design Excel Sum Formula
// https://leetcode.com/problems/design-excel-sum-formula/

class Excel(height: Int, width: Char) {
    private val values = Array(height + 1) { IntArray(width - 'A' + 1) }
    private val formulas = HashMap<Long, List<IntArray>>()

    fun set(row: Int, column: Char, `val`: Int) {
        val col = column - 'A'
        formulas.remove(key(row, col))
        values[row][col] = `val`
    }

    fun get(row: Int, column: Char): Int = eval(row, column - 'A')

    fun sum(row: Int, column: Char, numbers: Array<String>): Int {
        val col = column - 'A'
        val cells = ArrayList<IntArray>()
        for (token in numbers) {
            val colon = token.indexOf(':')
            if (colon >= 0) {
                val p1 = parse(token.substring(0, colon))
                val p2 = parse(token.substring(colon + 1))
                for (r in p1[0]..p2[0]) {
                    for (c in p1[1]..p2[1]) {
                        cells.add(intArrayOf(r, c))
                    }
                }
            } else {
                cells.add(parse(token))
            }
        }
        formulas[key(row, col)] = cells
        return eval(row, col)
    }

    private fun parse(cell: String): IntArray =
        intArrayOf(cell.substring(1).toInt(), cell[0] - 'A')

    private fun eval(row: Int, col: Int): Int {
        val formula = formulas[key(row, col)]
        if (formula != null) {
            var total = 0
            for (cell in formula) total += eval(cell[0], cell[1])
            return total
        }
        return values[row][col]
    }

    private fun key(row: Int, col: Int): Long =
        (row.toLong() shl 32) or (col.toLong() and 0xffffffffL)
}
