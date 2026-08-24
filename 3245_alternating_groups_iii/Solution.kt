// LeetCode 3245 - Alternating Groups III
// https://leetcode.com/problems/alternating-groups-iii/

class Solution {
    private class SegTree(private val n: Int) {
        private val treeIntervalCounts = IntArray(4 * n)
        private val treeIntervalLengths = IntArray(4 * n)

        fun add(i: Int, `val`: Int) {
            addRec(0, 0, n - 1, i, `val`)
        }

        private fun addRec(treeIndex: Int, lo: Int, hi: Int, i: Int, `val`: Int) {
            if (lo == hi) {
                treeIntervalCounts[treeIndex] += `val`
                treeIntervalLengths[treeIndex] = treeIntervalCounts[treeIndex] * i
                return
            }
            val mid = (lo + hi) / 2
            if (i <= mid) {
                addRec(2 * treeIndex + 1, lo, mid, i, `val`)
            } else {
                addRec(2 * treeIndex + 2, mid + 1, hi, i, `val`)
            }
            treeIntervalCounts[treeIndex] =
                treeIntervalCounts[2 * treeIndex + 1] + treeIntervalCounts[2 * treeIndex + 2]
            treeIntervalLengths[treeIndex] =
                treeIntervalLengths[2 * treeIndex + 1] + treeIntervalLengths[2 * treeIndex + 2]
        }

        fun queryIntervalCounts(i: Int): Int =
            query(treeIntervalCounts, 0, 0, n - 1, i, n - 1)

        fun queryIntervalLengths(i: Int): Int =
            query(treeIntervalLengths, 0, 0, n - 1, i, n - 1)

        private fun query(tree: IntArray, treeIndex: Int, lo: Int, hi: Int, i: Int, j: Int): Int {
            if (i <= lo && hi <= j) return tree[treeIndex]
            if (j < lo || hi < i) return 0
            val mid = (lo + hi) / 2
            return query(tree, treeIndex * 2 + 1, lo, mid, i, j) +
                query(tree, treeIndex * 2 + 2, mid + 1, hi, i, j)
        }
    }

    private fun pack(l: Int, r: Int): Long =
        (l.toLong() shl 32) or (r.toLong() and 0xffffffffL)

    private fun unpackL(v: Long): Int = (v shr 32).toInt()

    private fun unpackR(v: Long): Int = v.toInt()

    fun numberOfAlternatingGroups(colors: IntArray, queries: Array<IntArray>): IntArray {
        val n = colors.size
        val ans = ArrayList<Int>()
        val arr = IntArray(2 * n - 1)
        for (i in 0 until n) arr[i] = colors[i]
        for (i in 0 until n - 1) arr[n + i] = colors[i]
        val tree = SegTree(2 * n - 1)
        val intervals = sortedSetOf<Long>()

        fun insert(l: Int, r: Int) {
            intervals.add(pack(l, r))
            if (l < n) tree.add(r - l + 1, 1)
        }

        fun remove(l: Int, r: Int) {
            intervals.remove(pack(l, r))
            if (l < n) tree.add(r - l + 1, -1)
        }

        fun findInterval(target: Int): IntArray {
            var bestL = -1
            var bestR = -1
            for (k in intervals) {
                val kl = unpackL(k)
                val kr = unpackR(k)
                if (kl <= target && target <= kr) {
                    if (kl > bestL) {
                        bestL = kl
                        bestR = kr
                    }
                }
            }
            return intArrayOf(bestL, bestR)
        }

        fun getNum(sz: Int): Int {
            val numIntervals = tree.queryIntervalCounts(sz)
            val sumIntervals = tree.queryIntervalLengths(sz)
            var numAlternatingGroups = sumIntervals - numIntervals * sz + numIntervals
            val lr = findInterval(n)
            val l = lr[0]
            val r = lr[1]
            if (l < 0 || l >= n || r - l + 1 < sz) return numAlternatingGroups
            if (r >= n) {
                val nonDuplicateGroups = n - l
                val numGroups = (r - l + 1) - sz + 1
                val extra = numGroups - nonDuplicateGroups
                if (extra > 0) numAlternatingGroups -= extra
            }
            return numAlternatingGroups
        }

        fun update(index: Int, color: Int) {
            if (arr[index] == color) return
            arr[index] = color
            val se = findInterval(index)
            val start = se[0]
            val end = se[1]
            remove(start, end)
            if (start < index && index < end) {
                insert(start, index - 1)
                insert(index, index)
                insert(index + 1, end)
                return
            }
            if (start == index && index < end) insert(start + 1, end)
            if (start < index && index == end) insert(start, end - 1)
            var ns = index
            var ne = index
            while (true) {
                var merged = false
                for (k in ArrayList(intervals)) {
                    val kl = unpackL(k)
                    val kr = unpackR(k)
                    if (kr + 1 == ns && arr[kr] != arr[ns]) {
                        remove(kl, kr)
                        ns = kl
                        merged = true
                        break
                    }
                }
                if (!merged) break
            }
            while (true) {
                var merged = false
                for (k in ArrayList(intervals)) {
                    val kl = unpackL(k)
                    val kr = unpackR(k)
                    if (kl == ne + 1 && arr[kl] != arr[ne]) {
                        remove(kl, kr)
                        ne = kr
                        merged = true
                        break
                    }
                }
                if (!merged) break
            }
            insert(ns, ne)
        }

        var st = 0
        for (i in 1 until 2 * n - 1) {
            if (arr[i] == arr[i - 1]) {
                insert(st, i - 1)
                st = i
            }
        }
        insert(st, 2 * n - 2)

        for (query in queries) {
            if (query[0] == 1) {
                ans.add(getNum(query[1]))
            } else {
                val index = query[1]
                val color = query[2]
                if (arr[index] != color) {
                    update(index, color)
                    if (index < n - 1) update(index + n, color)
                }
            }
        }
        return ans.toIntArray()
    }
}
