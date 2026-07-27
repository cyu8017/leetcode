// LeetCode 1634 - Add Two Polynomials Represented as Linked Lists
// https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/

class PolyNode(var coefficient: Int = 0, var power: Int = 0, var next: PolyNode? = null)

class Solution {
    fun addPoly(poly1: Any?, poly2: Any?): Any? {
        val listMode = poly1 is List<*> || poly2 is Array<*> || poly1 is Array<*> || poly2 is List<*>
        fun build(items: Any?): PolyNode? {
            val dummy = PolyNode()
            var cur = dummy
            val seq: List<Any?> = when (items) {
                is List<*> -> items
                is Array<*> -> items.toList()
                else -> emptyList()
            }
            for (item in seq) {
                val pair = when (item) {
                    is IntArray -> item[0] to item[1]
                    is List<*> -> (item[0] as Number).toInt() to (item[1] as Number).toInt()
                    is Array<*> -> (item[0] as Number).toInt() to (item[1] as Number).toInt()
                    else -> continue
                }
                cur.next = PolyNode(pair.first, pair.second)
                cur = cur.next!!
            }
            return dummy.next
        }
        var p1: PolyNode? = when (poly1) {
            is PolyNode -> poly1
            is List<*>, is Array<*> -> build(poly1)
            else -> null
        }
        var p2: PolyNode? = when (poly2) {
            is PolyNode -> poly2
            is List<*>, is Array<*> -> build(poly2)
            else -> null
        }
        val dummy = PolyNode()
        var cur = dummy
        while (p1 != null || p2 != null) {
            val c: Int
            val p: Int
            if (p2 == null || (p1 != null && p1.power > p2.power)) {
                c = p1!!.coefficient
                p = p1.power
                p1 = p1.next
            } else if (p1 == null || p2.power > p1.power) {
                c = p2!!.coefficient
                p = p2.power
                p2 = p2.next
            } else {
                c = p1!!.coefficient + p2.coefficient
                p = p1.power
                p1 = p1.next
                p2 = p2.next
            }
            if (c != 0) {
                cur.next = PolyNode(c, p)
                cur = cur.next!!
            }
        }
        if (!listMode) return dummy.next
        val out = mutableListOf<IntArray>()
        var node = dummy.next
        while (node != null) {
            out.add(intArrayOf(node.coefficient, node.power))
            node = node.next
        }
        return out.toTypedArray()
    }
}
