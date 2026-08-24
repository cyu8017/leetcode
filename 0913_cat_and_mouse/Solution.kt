// LeetCode 0913 - Cat and Mouse
// https://leetcode.com/problems/cat-and-mouse/

class Solution {
    fun catMouseGame(graph: Array<IntArray>): Int {
        var n = graph.size
        var DRAW = 0
        var MOUSE_WIN = 1
        var CAT_WIN = 2
        int[][][] states = Array(n) { Array(n) { IntArray(2) } }
        int[][][] outDegree = Array(n) { Array(n) { IntArray(2) } }
        var q = ArrayDeque()
        for (cat in 0 until n) {
            for (mouse in 0 until n) {
                outDegree[cat][mouse][0] = graph[mouse].length
                var deg = 0
                for (x in graph[cat]) { if (x != 0) deg++; }
                outDegree[cat][mouse][1] = deg
            }
        }
        for (cat in 1 until n) {
            for (move in 0 until 2) {
                states[cat][0][move] = MOUSE_WIN
                q.add(intArrayOf(cat, 0, move, MOUSE_WIN))
                states[cat][cat][move] = CAT_WIN
                q.add(intArrayOf(cat, cat, move, CAT_WIN))
            }
        }
        while (!q.isEmpty()) {
            var cur = q.removeFirst()
            var cat = cur[0]
            var mouse = cur[1]
            var move = cur[2]
            var state = cur[3]
            if (cat == 2 && mouse == 1 && move == 0) return state
            var prevMove = move ^ 1
            for (prev in graph[if (prevMove == 1) cat else mouse]) {
                var prevCat = if (prevMove == 1) prev else cat
                if (prevCat == 0) continue
                var prevMouse = if (prevMove == 1) mouse else prev
                if (states[prevCat][prevMouse][prevMove] != 0) continue
                if ((prevMove == 0 && state == MOUSE_WIN) ||
                    (prevMove == 1 && state == CAT_WIN) ||
                    outDegree[prevCat][prevMouse][prevMove] == 1) {
                    states[prevCat][prevMouse][prevMove] = state
                    q.add(intArrayOf(prevCat, prevMouse, prevMove, state))
                } else {
                    outDegree[prevCat][prevMouse][prevMove]--
                }
            }
        }
        return states[2][1][0]
    }
}
