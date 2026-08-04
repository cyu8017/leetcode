#!/usr/bin/env python3
"""Port Kotlin solutions for problems 1458-1499 (selected stubs)."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SOLUTIONS: dict[str, str] = {}

SOLUTIONS["1458_max_dot_product_of_two_subsequences"] = r'''
// LeetCode 1458 - Max Dot Product of Two Subsequences
// https://leetcode.com/problems/max-dot-product-of-two-subsequences/

class Solution {
    fun maxDotProduct(nums1: IntArray, nums2: IntArray): Int {
        val n = nums2.size
        val dp = LongArray(n + 1) { Long.MIN_VALUE / 4 }
        for (a in nums1) {
            val prev = dp.copyOf()
            for (j in 1..n) {
                val product = a.toLong() * nums2[j - 1]
                dp[j] = maxOf(
                    dp[j - 1],
                    prev[j],
                    product,
                    product + maxOf(0L, prev[j - 1])
                )
            }
        }
        return dp[n].toInt()
    }
}
'''

SOLUTIONS["1460_make_two_arrays_equal_by_reversing_subarrays"] = r'''
// LeetCode 1460 - Make Two Arrays Equal by Reversing Subarrays
// https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

class Solution {
    fun canBeEqual(target: IntArray, arr: IntArray): Boolean {
        val a = target.copyOf().also { it.sort() }
        val b = arr.copyOf().also { it.sort() }
        return a.contentEquals(b)
    }
}
'''

SOLUTIONS["1461_check_if_a_string_contains_all_binary_codes_of_size_k"] = r'''
// LeetCode 1461 - Check If a String Contains All Binary Codes of Size K
// https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

class Solution {
    fun hasAllCodes(s: String, k: Int): Boolean {
        if (s.length < k) return false
        val set = HashSet<String>()
        for (i in 0..s.length - k) {
            set.add(s.substring(i, i + k))
        }
        return set.size == (1 shl k)
    }
}
'''

SOLUTIONS["1462_course_schedule_iv"] = r'''
// LeetCode 1462 - Course Schedule IV
// https://leetcode.com/problems/course-schedule-iv/

class Solution {
    fun checkIfPrerequisite(numCourses: Int, prerequisites: Array<IntArray>, queries: Array<IntArray>): List<Boolean> {
        val reach = Array(numCourses) { BooleanArray(numCourses) }
        for (e in prerequisites) reach[e[0]][e[1]] = true
        for (k in 0 until numCourses) {
            for (i in 0 until numCourses) {
                if (reach[i][k]) {
                    for (j in 0 until numCourses) {
                        reach[i][j] = reach[i][j] || reach[k][j]
                    }
                }
            }
        }
        return queries.map { reach[it[0]][it[1]] }
    }
}
'''

SOLUTIONS["1463_cherry_pickup_ii"] = r'''
// LeetCode 1463 - Cherry Pickup II
// https://leetcode.com/problems/cherry-pickup-ii/

class Solution {
    fun cherryPickup(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        var dp = HashMap<Long, Int>()
        dp[key(0, n - 1)] = grid[0][0] + if (n > 1) grid[0][n - 1] else 0
        for (r in 1 until m) {
            val nxt = HashMap<Long, Int>()
            for ((k, score) in dp) {
                val a = (k shr 32).toInt()
                val b = k.toInt()
                for (na in a - 1..a + 1) {
                    for (nb in b - 1..b + 1) {
                        if (na !in 0 until n || nb !in 0 until n) continue
                        val value = score + grid[r][na] + if (na != nb) grid[r][nb] else 0
                        val nk = key(na, nb)
                        nxt[nk] = maxOf(nxt.getOrDefault(nk, -1), value)
                    }
                }
            }
            dp = nxt
        }
        return dp.values.maxOrNull() ?: 0
    }

    private fun key(a: Int, b: Int): Long = (a.toLong() shl 32) or (b.toLong() and 0xffffffffL)
}
'''

SOLUTIONS["1464_maximum_product_of_two_elements_in_an_array"] = r'''
// LeetCode 1464 - Maximum Product of Two Elements in an Array
// https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution {
    fun maxProduct(nums: IntArray): Int {
        nums.sort()
        val n = nums.size
        return (nums[n - 2] - 1) * (nums[n - 1] - 1)
    }
}
'''

SOLUTIONS["1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts"] = r'''
// LeetCode 1465 - Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
// https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

class Solution {
    fun maxArea(h: Int, w: Int, horizontalCuts: IntArray, verticalCuts: IntArray): Int {
        val hs = IntArray(horizontalCuts.size + 2)
        hs[0] = 0
        hs[hs.size - 1] = h
        System.arraycopy(horizontalCuts, 0, hs, 1, horizontalCuts.size)
        hs.sort()
        val vs = IntArray(verticalCuts.size + 2)
        vs[0] = 0
        vs[vs.size - 1] = w
        System.arraycopy(verticalCuts, 0, vs, 1, verticalCuts.size)
        vs.sort()
        var maxH = 0L
        var maxV = 0L
        for (i in 1 until hs.size) maxH = maxOf(maxH, (hs[i] - hs[i - 1]).toLong())
        for (i in 1 until vs.size) maxV = maxOf(maxV, (vs[i] - vs[i - 1]).toLong())
        return ((maxH * maxV) % 1_000_000_007L).toInt()
    }
}
'''

SOLUTIONS["1466_reorder_routes_to_make_all_paths_lead_to_the_city_zero"] = r'''
// LeetCode 1466 - Reorder Routes to Make All Paths Lead to the City Zero
// https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

class Solution {
    fun minReorder(n: Int, connections: Array<IntArray>): Int {
        val graph = Array(n) { mutableListOf<IntArray>() }
        for (e in connections) {
            graph[e[0]].add(intArrayOf(e[1], 1))
            graph[e[1]].add(intArrayOf(e[0], 0))
        }
        var ans = 0
        val stack = ArrayDeque<Int>()
        val seen = BooleanArray(n)
        stack.add(0)
        seen[0] = true
        while (stack.isNotEmpty()) {
            val node = stack.removeLast()
            for (edge in graph[node]) {
                val nei = edge[0]
                val cost = edge[1]
                if (!seen[nei]) {
                    seen[nei] = true
                    stack.add(nei)
                    ans += cost
                }
            }
        }
        return ans
    }
}
'''

SOLUTIONS["1467_probability_of_a_two_boxes_having_the_same_number_of_distinct_balls"] = r'''
// LeetCode 1467 - Probability of a Two Boxes Having the Same Number of Distinct Balls
// https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/

class Solution {
    private var good = 0L
    private var total = 0L
    private var half = 0
    private lateinit var balls: IntArray
    private lateinit var comb: Array<LongArray>

    fun getProbability(balls: IntArray): Double {
        this.balls = balls
        half = balls.sum() / 2
        val max = balls.maxOrNull() ?: 0
        comb = Array(max + 1) { LongArray(max + 1) }
        for (i in 0..max) {
            comb[i][0] = 1
            comb[i][i] = 1
            for (j in 1 until i) {
                comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j]
            }
        }
        good = 0
        total = 0
        dfs(0, 0, 0, 1L)
        return good.toDouble() / total
    }

    private fun dfs(i: Int, left: Int, dl: Int, ways: Long) {
        if (i == balls.size) {
            if (left == half) {
                total += ways
                if (dl == 0) good += ways
            }
            return
        }
        for (x in 0..balls[i]) {
            if (left + x <= half) {
                val delta = (if (x > 0) 1 else 0) - (if (x < balls[i]) 1 else 0)
                dfs(i + 1, left + x, dl + delta, ways * comb[balls[i]][x])
            }
        }
    }
}
'''

SOLUTIONS["1469_find_all_the_lonely_nodes"] = r'''
// LeetCode 1469 - Find All The Lonely Nodes
// https://leetcode.com/problems/find-all-the-lonely-nodes/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun getLonelyNodes(root: TreeNode?): List<Int> {
        val ans = mutableListOf<Int>()
        fun dfs(node: TreeNode?) {
            if (node == null) return
            val left = node.left
            val right = node.right
            if ((left != null) xor (right != null)) {
                ans.add((left ?: right)!!.`val`)
            }
            dfs(left)
            dfs(right)
        }
        dfs(root)
        return ans
    }
}
'''

SOLUTIONS["1470_shuffle_the_array"] = r'''
// LeetCode 1470 - Shuffle the Array
// https://leetcode.com/problems/shuffle-the-array/

class Solution {
    fun shuffle(nums: IntArray, n: Int): IntArray {
        val ans = IntArray(2 * n)
        for (i in 0 until n) {
            ans[2 * i] = nums[i]
            ans[2 * i + 1] = nums[n + i]
        }
        return ans
    }
}
'''

SOLUTIONS["1471_the_k_strongest_values_in_an_array"] = r'''
// LeetCode 1471 - The k Strongest Values in an Array
// https://leetcode.com/problems/the-k-strongest-values-in-an-array/

class Solution {
    fun getStrongest(arr: IntArray, k: Int): IntArray {
        arr.sort()
        val median = arr[(arr.size - 1) / 2]
        val sorted = arr.sortedWith(compareByDescending<Int> { kotlin.math.abs(it - median) }.thenByDescending { it })
        return sorted.take(k).toIntArray()
    }
}
'''

SOLUTIONS["1472_design_browser_history"] = r'''
// LeetCode 1472 - Design Browser History
// https://leetcode.com/problems/design-browser-history/

class BrowserHistory(homepage: String) {
    private val history = mutableListOf(homepage)
    private var index = 0

    fun visit(url: String) {
        while (history.size > index + 1) history.removeAt(history.lastIndex)
        history.add(url)
        index++
    }

    fun back(steps: Int): String {
        index = maxOf(0, index - steps)
        return history[index]
    }

    fun forward(steps: Int): String {
        index = minOf(history.size - 1, index + steps)
        return history[index]
    }
}
'''

SOLUTIONS["1473_paint_house_iii"] = r'''
// LeetCode 1473 - Paint House III
// https://leetcode.com/problems/paint-house-iii/

class Solution {
    fun minCost(houses: IntArray, cost: Array<IntArray>, m: Int, n: Int, target: Int): Int {
        val inf = 1e15.toLong()
        var dp = HashMap<Long, Long>()
        dp[key(0, 0)] = 0L
        for (i in houses.indices) {
            val painted = houses[i]
            val nxt = HashMap<Long, Long>()
            val colors = if (painted != 0) listOf(painted) else (1..n).toList()
            for ((state, value) in dp) {
                val prev = (state shr 32).toInt()
                val groups = state.toInt()
                for (color in colors) {
                    val ng = groups + if (color != prev) 1 else 0
                    if (ng <= target) {
                        val nv = value + if (painted != 0) 0L else cost[i][color - 1].toLong()
                        val nk = key(color, ng)
                        nxt[nk] = minOf(nxt.getOrDefault(nk, inf), nv)
                    }
                }
            }
            dp = nxt
        }
        var ans = inf
        for ((state, value) in dp) {
            if (state.toInt() == target) ans = minOf(ans, value)
        }
        return if (ans == inf) -1 else ans.toInt()
    }

    private fun key(a: Int, b: Int): Long = (a.toLong() shl 32) or (b.toLong() and 0xffffffffL)
}
'''

SOLUTIONS["1474_delete_n_nodes_after_m_nodes_of_a_linked_list"] = r'''
// LeetCode 1474 - Delete N Nodes After M Nodes of a Linked List
// https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun deleteNodes(head: ListNode?, m: Int, n: Int): ListNode? {
        var cur = head
        while (cur != null) {
            repeat(m - 1) {
                if (cur == null) return@repeat
                cur = cur!!.next
            }
            if (cur == null) break
            var drop = cur!!.next
            repeat(n) {
                if (drop != null) drop = drop!!.next
            }
            cur!!.next = drop
            cur = drop
        }
        return head
    }
}
'''

SOLUTIONS["1475_final_prices_with_a_special_discount_in_a_shop"] = r'''
// LeetCode 1475 - Final Prices With a Special Discount in a Shop
// https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

class Solution {
    fun finalPrices(prices: IntArray): IntArray {
        val ans = prices.copyOf()
        val stack = ArrayDeque<Int>()
        for (i in prices.indices) {
            while (stack.isNotEmpty() && prices[stack.last()] >= prices[i]) {
                val j = stack.removeLast()
                ans[j] -= prices[i]
            }
            stack.add(i)
        }
        return ans
    }
}
'''

SOLUTIONS["1476_subrectangle_queries"] = r'''
// LeetCode 1476 - Subrectangle Queries
// https://leetcode.com/problems/subrectangle-queries/

class SubrectangleQueries(rectangle: Array<IntArray>) {
    private val rectangle = rectangle

    fun updateSubrectangle(row1: Int, col1: Int, row2: Int, col2: Int, newValue: Int) {
        for (r in row1..row2) {
            for (c in col1..col2) {
                rectangle[r][c] = newValue
            }
        }
    }

    fun getValue(row: Int, col: Int): Int = rectangle[row][col]
}
'''

SOLUTIONS["1477_find_two_non_overlapping_sub_arrays_each_with_target_sum"] = r'''
// LeetCode 1477 - Find Two Non-overlapping Sub-arrays Each With Target Sum
// https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

class Solution {
    fun minSumOfLengths(arr: IntArray, target: Int): Int {
        val inf = 1_000_000_000
        var left = 0
        var total = 0
        var best = inf
        var ans = inf
        val shortest = IntArray(arr.size) { inf }
        for (right in arr.indices) {
            total += arr[right]
            while (total > target) {
                total -= arr[left]
                left++
            }
            if (total == target) {
                val length = right - left + 1
                if (left > 0) ans = minOf(ans, length + shortest[left - 1])
                best = minOf(best, length)
            }
            shortest[right] = best
        }
        return if (ans == inf) -1 else ans
    }
}
'''

SOLUTIONS["1478_allocate_mailboxes"] = r'''
// LeetCode 1478 - Allocate Mailboxes
// https://leetcode.com/problems/allocate-mailboxes/

class Solution {
    fun minDistance(houses: IntArray, k: Int): Int {
        houses.sort()
        val n = houses.size
        val cost = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            for (j in i until n) {
                val mid = houses[(i + j) / 2]
                var sum = 0
                for (t in i..j) sum += kotlin.math.abs(houses[t] - mid)
                cost[i][j] = sum
            }
        }
        val inf = 1e15.toLong()
        var dp = LongArray(n + 1) { inf }
        dp[0] = 0
        repeat(k) {
            val ndp = LongArray(n + 1) { inf }
            ndp[0] = 0
            for (j in 1..n) {
                var best = inf
                for (i in 0 until j) {
                    best = minOf(best, dp[i] + cost[i][j - 1])
                }
                ndp[j] = best
            }
            dp = ndp
        }
        return dp[n].toInt()
    }
}
'''

SOLUTIONS["1480_running_sum_of_1d_array"] = r'''
// LeetCode 1480 - Running Sum of 1d Array
// https://leetcode.com/problems/running-sum-of-1d-array/

class Solution {
    fun runningSum(nums: IntArray): IntArray {
        for (i in 1 until nums.size) nums[i] += nums[i - 1]
        return nums
    }
}
'''

SOLUTIONS["1481_least_number_of_unique_integers_after_k_removals"] = r'''
// LeetCode 1481 - Least Number of Unique Integers after K Removals
// https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

class Solution {
    fun findLeastNumOfUniqueInts(arr: IntArray, k: Int): Int {
        val freq = HashMap<Int, Int>()
        for (x in arr) freq[x] = freq.getOrDefault(x, 0) + 1
        val counts = freq.values.sorted()
        var remaining = k
        var removed = 0
        for (count in counts) {
            if (remaining < count) break
            remaining -= count
            removed++
        }
        return counts.size - removed
    }
}
'''

SOLUTIONS["1482_minimum_number_of_days_to_make_m_bouquets"] = r'''
// LeetCode 1482 - Minimum Number of Days to Make m Bouquets
// https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution {
    fun minDays(bloomDay: IntArray, m: Int, k: Int): Int {
        if (m.toLong() * k > bloomDay.size) return -1
        fun possible(day: Int): Boolean {
            var bouquets = 0
            var run = 0
            for (x in bloomDay) {
                run = if (x <= day) run + 1 else 0
                if (run == k) {
                    bouquets++
                    run = 0
                }
            }
            return bouquets >= m
        }
        var lo = bloomDay.minOrNull()!!
        var hi = bloomDay.maxOrNull()!!
        while (lo < hi) {
            val mid = lo + (hi - lo) / 2
            if (possible(mid)) hi = mid else lo = mid + 1
        }
        return lo
    }
}
'''

SOLUTIONS["1483_kth_ancestor_of_a_tree_node"] = r'''
// LeetCode 1483 - Kth Ancestor of a Tree Node
// https://leetcode.com/problems/kth-ancestor-of-a-tree-node/

class TreeAncestor(n: Int, parent: IntArray) {
    private val up: Array<IntArray>

    init {
        val width = maxOf(1, 32 - Integer.numberOfLeadingZeros(n))
        up = Array(width) { IntArray(n) { -1 } }
        for (i in 0 until n) up[0][i] = parent[i]
        for (bit in 1 until width) {
            for (i in 0 until n) {
                val p = up[bit - 1][i]
                up[bit][i] = if (p == -1) -1 else up[bit - 1][p]
            }
        }
    }

    fun getKthAncestor(node: Int, k: Int): Int {
        var cur = node
        var steps = k
        var bit = 0
        while (steps > 0 && cur != -1) {
            if (steps and 1 == 1) {
                if (bit >= up.size) return -1
                cur = up[bit][cur]
            }
            bit++
            steps = steps shr 1
        }
        return cur
    }
}
'''

SOLUTIONS["1485_clone_binary_tree_with_random_pointer"] = r'''
// LeetCode 1485 - Clone Binary Tree With Random Pointer
// https://leetcode.com/problems/clone-binary-tree-with-random-pointer/

class Node(var `val`: Int) {
    var left: Node? = null
    var right: Node? = null
    var random: Node? = null
}

class Solution {
    private val copies = HashMap<Node, Node>()

    fun copyRandomBinaryTree(root: Node?): Node? {
        if (root == null) return null
        if (root in copies) return copies[root]
        val copy = Node(root.`val`)
        copies[root] = copy
        copy.left = copyRandomBinaryTree(root.left)
        copy.right = copyRandomBinaryTree(root.right)
        copy.random = copyRandomBinaryTree(root.random)
        return copy
    }
}
'''

SOLUTIONS["1486_xor_operation_in_an_array"] = r'''
// LeetCode 1486 - XOR Operation in an Array
// https://leetcode.com/problems/xor-operation-in-an-array/

class Solution {
    fun xorOperation(n: Int, start: Int): Int {
        var ans = 0
        for (i in 0 until n) ans = ans xor (start + 2 * i)
        return ans
    }
}
'''

SOLUTIONS["1487_making_file_names_unique"] = r'''
// LeetCode 1487 - Making File Names Unique
// https://leetcode.com/problems/making-file-names-unique/

class Solution {
    fun getFolderNames(names: Array<String>): Array<String> {
        val used = HashMap<String, Int>()
        val ans = Array(names.size) { "" }
        for (i in names.indices) {
            val name = names[i]
            val candidate = if (name !in used) {
                name
            } else {
                var k = used[name]!!
                while ("$name($k)" in used) k++
                used[name] = k + 1
                "$name($k)"
            }
            used[candidate] = 1
            ans[i] = candidate
        }
        return ans
    }
}
'''

SOLUTIONS["1488_avoid_flood_in_the_city"] = r'''
// LeetCode 1488 - Avoid Flood in The City
// https://leetcode.com/problems/avoid-flood-in-the-city/

class Solution {
    fun avoidFlood(rains: IntArray): IntArray {
        val ans = IntArray(rains.size) { -1 }
        val full = HashMap<Int, Int>()
        val dry = java.util.TreeSet<Int>()
        for (i in rains.indices) {
            val lake = rains[i]
            if (lake == 0) {
                dry.add(i)
                ans[i] = 1
            } else {
                if (lake in full) {
                    val day = dry.higher(full[lake]!!) ?: return IntArray(0)
                    ans[day] = lake
                    dry.remove(day)
                }
                full[lake] = i
            }
        }
        return ans
    }
}
'''

SOLUTIONS["1489_find_critical_and_pseudo_critical_edges_in_minimum_spanning_tree"] = r'''
// LeetCode 1489 - Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
// https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/

class Solution {
    fun findCriticalAndPseudoCriticalEdges(n: Int, edges: Array<IntArray>): List<List<Int>> {
        val es = edges.mapIndexed { i, e -> intArrayOf(e[2], e[0], e[1], i) }
            .sortedWith(compareBy { it[0] })

        fun mst(skip: Int = -1, force: Int = -1): Long {
            val parent = IntArray(n) { it }
            fun find(x: Int): Int {
                var cur = x
                while (cur != parent[cur]) {
                    parent[cur] = parent[parent[cur]]
                    cur = parent[cur]
                }
                return cur
            }
            var total = 0L
            var used = 0
            if (force >= 0) {
                val e = es[force]
                parent[find(e[1])] = find(e[2])
                total += e[0]
                used++
            }
            for (j in es.indices) {
                if (j == skip || j == force) continue
                val e = es[j]
                val x = find(e[1])
                val y = find(e[2])
                if (x != y) {
                    parent[x] = y
                    total += e[0]
                    used++
                }
            }
            return if (used == n - 1) total else Long.MAX_VALUE / 4
        }

        val base = mst()
        val critical = mutableListOf<Int>()
        val pseudo = mutableListOf<Int>()
        for (j in es.indices) {
            if (mst(skip = j) > base) {
                critical.add(es[j][3])
            } else if (mst(force = j) == base) {
                pseudo.add(es[j][3])
            }
        }
        return listOf(critical.sorted(), pseudo.sorted())
    }
}
'''

SOLUTIONS["1490_clone_n_ary_tree"] = r'''
// LeetCode 1490 - Clone N-ary Tree
// https://leetcode.com/problems/clone-n-ary-tree/

class Node(var `val`: Int) {
    var children: MutableList<Node> = mutableListOf()
}

class Solution {
    fun cloneTree(root: Node?): Node? {
        if (root == null) return null
        val copy = Node(root.`val`)
        for (child in root.children) {
            copy.children.add(cloneTree(child)!!)
        }
        return copy
    }
}
'''

SOLUTIONS["1491_average_salary_excluding_the_minimum_and_maximum_salary"] = r'''
// LeetCode 1491 - Average Salary Excluding the Minimum and Maximum Salary
// https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution {
    fun average(salary: IntArray): Double {
        return (salary.sum().toLong() - salary.minOrNull()!! - salary.maxOrNull()!!).toDouble() / (salary.size - 2)
    }
}
'''

SOLUTIONS["1492_the_kth_factor_of_n"] = r'''
// LeetCode 1492 - The kth Factor of n
// https://leetcode.com/problems/the-kth-factor-of-n/

class Solution {
    fun kthFactor(n: Int, k: Int): Int {
        var remaining = k
        for (x in 1..n) {
            if (n % x == 0) {
                remaining--
                if (remaining == 0) return x
            }
        }
        return -1
    }
}
'''

SOLUTIONS["1493_longest_subarray_of_1s_after_deleting_one_element"] = r'''
// LeetCode 1493 - Longest Subarray of 1's After Deleting One Element
// https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution {
    fun longestSubarray(nums: IntArray): Int {
        var left = 0
        var zeros = 0
        var ans = 0
        for (right in nums.indices) {
            if (nums[right] == 0) zeros++
            while (zeros > 1) {
                if (nums[left] == 0) zeros--
                left++
            }
            ans = maxOf(ans, right - left)
        }
        return ans
    }
}
'''

SOLUTIONS["1494_parallel_courses_ii"] = r'''
// LeetCode 1494 - Parallel Courses II
// https://leetcode.com/problems/parallel-courses-ii/

class Solution {
    fun minNumberOfSemesters(n: Int, relations: Array<IntArray>, k: Int): Int {
        val prereq = IntArray(n)
        for (e in relations) {
            prereq[e[1] - 1] = prereq[e[1] - 1] or (1 shl (e[0] - 1))
        }
        val full = (1 shl n) - 1
        val inf = 1_000_000_000
        val dp = IntArray(1 shl n) { inf }
        dp[0] = 0
        for (mask in 0 until (1 shl n)) {
            if (dp[mask] == inf) continue
            var available = 0
            for (c in 0 until n) {
                if ((mask shr c) and 1 == 0 && (prereq[c] and mask) == prereq[c]) {
                    available = available or (1 shl c)
                }
            }
            val choices = mutableListOf<Int>()
            if (Integer.bitCount(available) <= k) {
                choices.add(available)
            } else {
                var sub = available
                while (sub > 0) {
                    if (Integer.bitCount(sub) == k) choices.add(sub)
                    sub = (sub - 1) and available
                }
            }
            for (take in choices) {
                val next = mask or take
                dp[next] = minOf(dp[next], dp[mask] + 1)
            }
        }
        return dp[full]
    }
}
'''

SOLUTIONS["1496_path_crossing"] = r'''
// LeetCode 1496 - Path Crossing
// https://leetcode.com/problems/path-crossing/

class Solution {
    fun isPathCrossing(path: String): Boolean {
        var x = 0
        var y = 0
        val seen = HashSet<Long>()
        seen.add(0L)
        val move = mapOf('N' to (0 to 1), 'S' to (0 to -1), 'E' to (1 to 0), 'W' to (-1 to 0))
        for (c in path) {
            val (dx, dy) = move[c]!!
            x += dx
            y += dy
            val key = (x.toLong() shl 32) or (y.toLong() and 0xffffffffL)
            if (!seen.add(key)) return true
        }
        return false
    }
}
'''

SOLUTIONS["1497_check_if_array_pairs_are_divisible_by_k"] = r'''
// LeetCode 1497 - Check If Array Pairs Are Divisible by k
// https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution {
    fun canArrange(arr: IntArray, k: Int): Boolean {
        val count = IntArray(k)
        for (x in arr) {
            val r = ((x % k) + k) % k
            count[r]++
        }
        if (count[0] % 2 != 0) return false
        for (r in 1 until k) {
            if (count[r] != count[k - r]) return false
        }
        return true
    }
}
'''

SOLUTIONS["1498_number_of_subsequences_that_satisfy_the_given_sum_condition"] = r'''
// LeetCode 1498 - Number of Subsequences That Satisfy the Given Sum Condition
// https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution {
    fun numSubseq(nums: IntArray, target: Int): Int {
        nums.sort()
        val mod = 1_000_000_007
        val powers = IntArray(nums.size + 1)
        powers[0] = 1
        for (i in 1 until powers.size) powers[i] = (powers[i - 1] * 2) % mod
        var left = 0
        var right = nums.size - 1
        var ans = 0
        while (left <= right) {
            if (nums[left] + nums[right] <= target) {
                ans = (ans + powers[right - left]) % mod
                left++
            } else {
                right--
            }
        }
        return ans
    }
}
'''

SOLUTIONS["1499_max_value_of_equation"] = r'''
// LeetCode 1499 - Max Value of Equation
// https://leetcode.com/problems/max-value-of-equation/

class Solution {
    fun findMaxValueOfEquation(points: Array<IntArray>, k: Int): Int {
        val q = ArrayDeque<IntArray>()
        var ans = Int.MIN_VALUE / 2
        for (p in points) {
            val x = p[0]
            val y = p[1]
            while (q.isNotEmpty() && x - q.first()[0] > k) q.removeFirst()
            if (q.isNotEmpty()) ans = maxOf(ans, x + y + q.first()[1])
            val value = y - x
            while (q.isNotEmpty() && q.last()[1] <= value) q.removeLast()
            q.addLast(intArrayOf(x, value))
        }
        return ans
    }
}
'''


def main() -> None:
    expected = [
        "1458_max_dot_product_of_two_subsequences",
        "1460_make_two_arrays_equal_by_reversing_subarrays",
        "1461_check_if_a_string_contains_all_binary_codes_of_size_k",
        "1462_course_schedule_iv",
        "1463_cherry_pickup_ii",
        "1464_maximum_product_of_two_elements_in_an_array",
        "1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts",
        "1466_reorder_routes_to_make_all_paths_lead_to_the_city_zero",
        "1467_probability_of_a_two_boxes_having_the_same_number_of_distinct_balls",
        "1469_find_all_the_lonely_nodes",
        "1470_shuffle_the_array",
        "1471_the_k_strongest_values_in_an_array",
        "1472_design_browser_history",
        "1473_paint_house_iii",
        "1474_delete_n_nodes_after_m_nodes_of_a_linked_list",
        "1475_final_prices_with_a_special_discount_in_a_shop",
        "1476_subrectangle_queries",
        "1477_find_two_non_overlapping_sub_arrays_each_with_target_sum",
        "1478_allocate_mailboxes",
        "1480_running_sum_of_1d_array",
        "1481_least_number_of_unique_integers_after_k_removals",
        "1482_minimum_number_of_days_to_make_m_bouquets",
        "1483_kth_ancestor_of_a_tree_node",
        "1485_clone_binary_tree_with_random_pointer",
        "1486_xor_operation_in_an_array",
        "1487_making_file_names_unique",
        "1488_avoid_flood_in_the_city",
        "1489_find_critical_and_pseudo_critical_edges_in_minimum_spanning_tree",
        "1490_clone_n_ary_tree",
        "1491_average_salary_excluding_the_minimum_and_maximum_salary",
        "1492_the_kth_factor_of_n",
        "1493_longest_subarray_of_1s_after_deleting_one_element",
        "1494_parallel_courses_ii",
        "1496_path_crossing",
        "1497_check_if_array_pairs_are_divisible_by_k",
        "1498_number_of_subsequences_that_satisfy_the_given_sum_condition",
        "1499_max_value_of_equation",
    ]
    assert set(expected) == set(SOLUTIONS), (
        f"missing={set(expected)-set(SOLUTIONS)} extra={set(SOLUTIONS)-set(expected)}"
    )
    ported = 0
    for folder, body in SOLUTIONS.items():
        path = ROOT / folder / "Solution.kt"
        path.write_text(body.lstrip("\n"), encoding="utf-8")
        ported += 1
        print(f"wrote {folder}")
    print(f"ported={ported}")


if __name__ == "__main__":
    main()
