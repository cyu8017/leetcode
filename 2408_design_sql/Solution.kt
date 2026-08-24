// LeetCode 2408 - Design SQL
// https://leetcode.com/problems/design-sql/

class SQL(names: Array<String>, columns: IntArray) {
    private val tables = HashMap<String, ArrayList<ArrayList<String>>>()
    private val nextID = HashMap<String, Int>()

    init {
        for (name in names) {
            tables[name] = ArrayList()
            nextID[name] = 1
        }
    }

    fun ins(name: String, row: List<String>): Boolean {
        if (name !in tables) return false
        val id = nextID[name]!!
        nextID[name] = id + 1
        val full = ArrayList<String>()
        full.add(id.toString())
        full.addAll(row)
        tables[name]!!.add(full)
        return true
    }

    fun rmv(name: String, rowId: Int) {
        val rows = tables[name]!!
        for (i in rows.indices) {
            if (rows[i][0].toInt() == rowId) {
                rows.removeAt(i)
                return
            }
        }
    }

    fun sel(name: String, rowId: Int, columnId: Int): String {
        for (r in tables[name]!!) {
            if (r[0].toInt() == rowId) {
                if (columnId < 1 || columnId >= r.size) return "<null>"
                return r[columnId]
            }
        }
        return "<null>"
    }

    fun exp(name: String): List<String> {
        val ans = ArrayList<String>()
        for (r in tables[name]!!) {
            val sb = StringBuilder(r[0])
            for (j in 1 until r.size) sb.append(',').append(r[j])
            ans.add(sb.toString())
        }
        return ans
    }
}
