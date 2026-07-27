// LeetCode 1600 - Throne Inheritance
// https://leetcode.com/problems/throne-inheritance/

class ThroneInheritance(kingName: String) {
    private val king = kingName
    private val children = HashMap<String, MutableList<String>>()
    private val dead = HashSet<String>()

    fun birth(parentName: String, childName: String) {
        children.getOrPut(parentName) { mutableListOf() }.add(childName)
    }

    fun death(name: String) {
        dead.add(name)
    }

    fun getInheritanceOrder(): List<String> {
        val order = mutableListOf<String>()
        fun visit(name: String) {
            if (name !in dead) order.add(name)
            for (child in children[name].orEmpty()) visit(child)
        }
        visit(king)
        return order
    }
}
