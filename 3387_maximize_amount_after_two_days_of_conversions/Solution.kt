// LeetCode 3387 - Maximize Amount After Two Days of Conversions
// https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/

class Solution {
    private fun buildRateGraph(pairs: List<List<String>>, rates: DoubleArray): HashMap<String, HashMap<String, Double>> {
        val g = HashMap<String, HashMap<String, Double>>()
        for (i in pairs.indices) {
            val a = pairs[i][0]
            val b = pairs[i][1]
            g.getOrPut(a) { HashMap() }[b] = rates[i]
            g.getOrPut(b) { HashMap() }[a] = 1.0 / rates[i]
        }
        return g
    }

    private fun bellman(start: String, pairs: List<List<String>>, rates: DoubleArray): HashMap<String, Double> {
        val g = buildRateGraph(pairs, rates)
        val dist = HashMap<String, Double>()
        dist[start] = 1.0
        repeat(100) {
            var updated = false
            for ((from, neighbors) in g) {
                val fromDist = dist[from] ?: continue
                if (fromDist == 0.0) continue
                for ((to, rate) in neighbors) {
                    val nv = fromDist * rate
                    if (nv > (dist[to] ?: 0.0)) {
                        dist[to] = nv
                        updated = true
                    }
                }
            }
            if (!updated) return@repeat
        }
        return dist
    }

    fun maxAmount(
        initialCurrency: String,
        pairs1: List<List<String>>,
        rates1: DoubleArray,
        pairs2: List<List<String>>,
        rates2: DoubleArray,
    ): Double {
        val amt1 = bellman(initialCurrency, pairs1, rates1)
        var ans = 1.0
        val g2 = buildRateGraph(pairs2, rates2)
        for ((c, a) in amt1) {
            if (a <= 0) continue
            val dist = HashMap<String, Double>()
            dist[c] = a
            var updated = true
            var it = 0
            while (it < 100 && updated) {
                updated = false
                for ((from, neighbors) in g2) {
                    val fromDist = dist[from] ?: continue
                    if (fromDist == 0.0) continue
                    for ((to, rate) in neighbors) {
                        val nv = fromDist * rate
                        if (nv > (dist[to] ?: 0.0)) {
                            dist[to] = nv
                            updated = true
                        }
                    }
                }
                it++
            }
            val back = dist[initialCurrency]
            if (back != null && back > ans) ans = back
        }
        return ans
    }
}
