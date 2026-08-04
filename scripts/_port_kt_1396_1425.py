from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

solutions = {}

solutions["1396_design_underground_system"] = r"""// LeetCode 1396 - Design Underground System
// https://leetcode.com/problems/design-underground-system/

class UndergroundSystem {
    private val checkIns = HashMap<Int, Pair<String, Int>>()
    private val stats = HashMap<Pair<String, String>, LongArray>()

    fun checkIn(id: Int, stationName: String, t: Int) {
        checkIns[id] = stationName to t
    }

    fun checkOut(id: Int, stationName: String, t: Int) {
        val (start, begin) = checkIns.remove(id)!!
        val key = start to stationName
        val cur = stats.getOrPut(key) { longArrayOf(0L, 0L) }
        cur[0] += (t - begin).toLong()
        cur[1] += 1L
    }

    fun getAverageTime(startStation: String, endStation: String): Double {
        val cur = stats[startStation to endStation]!!
        return cur[0].toDouble() / cur[1]
    }
}
"""

solutions["1397_find_all_good_strings"] = r"""// LeetCode 1397 - Find All Good Strings
// https://leetcode.com/problems/find-all-good-strings/

class Solution {
    fun findGoodStrings(n: Int, s1: String, s2: String, evil: String): Int {
        val mod = 1_000_000_007
        val m = evil.length
        val pi = IntArray(m)
        for (i in 1 until m) {
            var j = pi[i - 1]
            while (j > 0 && evil[i] != evil[j]) j = pi[j - 1]
            if (evil[i] == evil[j]) j++
            pi[i] = j
        }
        val trans = Array(m) { IntArray(26) }
        for (j in 0 until m) {
            for (x in 0 until 26) {
                val c = ('a'.code + x).toChar()
                var k = j
                while (k > 0 && evil[k] != c) k = pi[k - 1]
                if (evil[k] == c) k++
                trans[j][x] = k
            }
        }
        val memo = HashMap<Long, Int>()
        fun key(i: Int, j: Int, lo: Boolean, hi: Boolean): Long {
            return (((i.toLong() * (m + 1) + j) * 2 + if (lo) 1 else 0) * 2) + if (hi) 1 else 0
        }
        fun dp(i: Int, j: Int, lo: Boolean, hi: Boolean): Int {
            if (j == m) return 0
            if (i == n) return 1
            val memoKey = key(i, j, lo, hi)
            memo[memoKey]?.let { return it }
            val a = if (lo) s1[i] - 'a' else 0
            val b = if (hi) s2[i] - 'a' else 25
            var ans = 0
            for (x in a..b) {
                ans = (ans + dp(i + 1, trans[j][x], lo && x == a, hi && x == b)) % mod
            }
            memo[memoKey] = ans
            return ans
        }
        return dp(0, 0, true, true)
    }
}
"""

solutions["1399_count_largest_group"] = r"""// LeetCode 1399 - Count Largest Group
// https://leetcode.com/problems/count-largest-group/

class Solution {
    fun countLargestGroup(n: Int): Int {
        val counts = HashMap<Int, Int>()
        for (x in 1..n) {
            var sum = 0
            var v = x
            while (v > 0) {
                sum += v % 10
                v /= 10
            }
            counts[sum] = counts.getOrDefault(sum, 0) + 1
        }
        val max = counts.values.maxOrNull() ?: 0
        return counts.values.count { it == max }
    }
}
"""

solutions["1400_construct_k_palindrome_strings"] = r"""// LeetCode 1400 - Construct K Palindrome Strings
// https://leetcode.com/problems/construct-k-palindrome-strings/

class Solution {
    fun canConstruct(s: String, k: Int): Boolean {
        if (k > s.length) return false
        val freq = IntArray(26)
        for (c in s) freq[c - 'a']++
        val odds = freq.count { it % 2 == 1 }
        return odds <= k
    }
}
"""

solutions["1401_circle_and_rectangle_overlapping"] = r"""// LeetCode 1401 - Circle and Rectangle Overlapping
// https://leetcode.com/problems/circle-and-rectangle-overlapping/

class Solution {
    fun checkOverlap(radius: Int, xCenter: Int, yCenter: Int, x1: Int, y1: Int, x2: Int, y2: Int): Boolean {
        val x = minOf(maxOf(xCenter, x1), x2)
        val y = minOf(maxOf(yCenter, y1), y2)
        val dx = x - xCenter
        val dy = y - yCenter
        return dx * dx + dy * dy <= radius * radius
    }
}
"""

solutions["1402_reducing_dishes"] = r"""// LeetCode 1402 - Reducing Dishes
// https://leetcode.com/problems/reducing-dishes/

class Solution {
    fun maxSatisfaction(satisfaction: IntArray): Int {
        satisfaction.sortDescending()
        var total = 0
        var answer = 0
        for (value in satisfaction) {
            if (total + value <= 0) break
            total += value
            answer += total
        }
        return answer
    }
}
"""

solutions["1403_minimum_subsequence_in_non_increasing_order"] = r"""// LeetCode 1403 - Minimum Subsequence in Non-Increasing Order
// https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

class Solution {
    fun minSubsequence(nums: IntArray): List<Int> {
        val sorted = nums.sortedDescending()
        val total = nums.sum()
        val answer = ArrayList<Int>()
        var chosen = 0
        for (value in sorted) {
            answer.add(value)
            chosen += value
            if (chosen > total - chosen) return answer
        }
        return answer
    }
}
"""

solutions["1404_number_of_steps_to_reduce_a_number_in_binary_representation_to_one"] = r"""// LeetCode 1404 - Number of Steps to Reduce a Number in Binary Representation to One
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

class Solution {
    fun numSteps(s: String): Int {
        var steps = 0
        var carry = 0
        for (i in s.length - 1 downTo 1) {
            val value = (s[i] - '0') + carry
            if (value == 1) {
                steps += 2
                carry = 1
            } else {
                steps += 1
            }
        }
        return steps + carry
    }
}
"""

solutions["1405_longest_happy_string"] = r"""// LeetCode 1405 - Longest Happy String
// https://leetcode.com/problems/longest-happy-string/

import java.util.PriorityQueue

class Solution {
    fun longestDiverseString(a: Int, b: Int, c: Int): String {
        val heap = PriorityQueue<IntArray>(compareByDescending { it[0] })
        if (a > 0) heap.offer(intArrayOf(a, 'a'.code))
        if (b > 0) heap.offer(intArrayOf(b, 'b'.code))
        if (c > 0) heap.offer(intArrayOf(c, 'c'.code))
        val answer = StringBuilder()
        while (heap.isNotEmpty()) {
            val cur = heap.poll()
            val len = answer.length
            if (len >= 2 && answer[len - 1].code == cur[1] && answer[len - 2].code == cur[1]) {
                if (heap.isEmpty()) break
                val next = heap.poll()
                answer.append(next[1].toChar())
                if (--next[0] > 0) heap.offer(next)
                heap.offer(cur)
            } else {
                answer.append(cur[1].toChar())
                if (--cur[0] > 0) heap.offer(cur)
            }
        }
        return answer.toString()
    }
}
"""

solutions["1406_stone_game_iii"] = r"""// LeetCode 1406 - Stone Game III
// https://leetcode.com/problems/stone-game-iii/

class Solution {
    fun stoneGameIII(stoneValue: IntArray): String {
        val n = stoneValue.size
        val dp = LongArray(n + 1)
        for (i in n - 1 downTo 0) {
            var take = 0L
            dp[i] = Long.MIN_VALUE / 4
            for (j in i until minOf(i + 3, n)) {
                take += stoneValue[j]
                dp[i] = maxOf(dp[i], take - dp[j + 1])
            }
        }
        return when {
            dp[0] > 0 -> "Alice"
            dp[0] < 0 -> "Bob"
            else -> "Tie"
        }
    }
}
"""

solutions["1408_string_matching_in_an_array"] = r"""// LeetCode 1408 - String Matching in an Array
// https://leetcode.com/problems/string-matching-in-an-array/

class Solution {
    fun stringMatching(words: Array<String>): List<String> {
        val answer = ArrayList<String>()
        for (i in words.indices) {
            for (j in words.indices) {
                if (i != j && words[j].contains(words[i])) {
                    answer.add(words[i])
                    break
                }
            }
        }
        return answer
    }
}
"""

solutions["1409_queries_on_a_permutation_with_key"] = r"""// LeetCode 1409 - Queries on a Permutation With Key
// https://leetcode.com/problems/queries-on-a-permutation-with-key/

class Solution {
    fun processQueries(queries: IntArray, m: Int): IntArray {
        val values = ArrayList((1..m).toList())
        val answer = IntArray(queries.size)
        for (qi in queries.indices) {
            val query = queries[qi]
            val index = values.indexOf(query)
            answer[qi] = index
            values.removeAt(index)
            values.add(0, query)
        }
        return answer
    }
}
"""

solutions["1410_html_entity_parser"] = r"""// LeetCode 1410 - HTML Entity Parser
// https://leetcode.com/problems/html-entity-parser/

class Solution {
    fun entityParser(text: String): String {
        var result = text
        result = result.replace("&quot;", "\"")
        result = result.replace("&apos;", "'")
        result = result.replace("&gt;", ">")
        result = result.replace("&lt;", "<")
        result = result.replace("&frasl;", "/")
        result = result.replace("&amp;", "&")
        return result
    }
}
"""

solutions["1411_number_of_ways_to_paint_n_3_grid"] = r"""// LeetCode 1411 - Number of Ways to Paint N x 3 Grid
// https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/

class Solution {
    fun numOfWays(n: Int): Int {
        val mod = 1_000_000_007L
        var aba = 6L
        var abc = 6L
        for (i in 1 until n) {
            val nextAba = (3 * aba + 2 * abc) % mod
            val nextAbc = (2 * aba + 2 * abc) % mod
            aba = nextAba
            abc = nextAbc
        }
        return ((aba + abc) % mod).toInt()
    }
}
"""

solutions["1413_minimum_value_to_get_positive_step_by_step_sum"] = r"""// LeetCode 1413 - Minimum Value to Get Positive Step by Step Sum
// https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

class Solution {
    fun minStartValue(nums: IntArray): Int {
        var prefix = 0
        var lowest = 0
        for (value in nums) {
            prefix += value
            lowest = minOf(lowest, prefix)
        }
        return 1 - lowest
    }
}
"""

solutions["1414_find_the_minimum_number_of_fibonacci_numbers_whose_sum_is_k"] = r"""// LeetCode 1414 - Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
// https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

class Solution {
    fun findMinFibonacciNumbers(k: Int): Int {
        var remaining = k
        val fib = arrayListOf(1, 1)
        while (fib.last() < remaining) {
            fib.add(fib[fib.size - 1] + fib[fib.size - 2])
        }
        var answer = 0
        for (i in fib.size - 1 downTo 0) {
            if (fib[i] <= remaining) {
                remaining -= fib[i]
                answer++
            }
        }
        return answer
    }
}
"""

solutions["1415_the_k_th_lexicographical_string_of_all_happy_strings_of_length_n"] = r"""// LeetCode 1415 - The k-th Lexicographical String of All Happy Strings of Length n
// https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

class Solution {
    fun getHappyString(n: Int, k: Int): String {
        val answer = ArrayList<String>()
        fun build(path: StringBuilder) {
            if (path.length == n) {
                answer.add(path.toString())
                return
            }
            for (char in "abc") {
                if (path.isEmpty() || path.last() != char) {
                    path.append(char)
                    build(path)
                    path.deleteCharAt(path.length - 1)
                }
            }
        }
        build(StringBuilder())
        return if (k <= answer.size) answer[k - 1] else ""
    }
}
"""

solutions["1416_restore_the_array"] = r"""// LeetCode 1416 - Restore The Array
// https://leetcode.com/problems/restore-the-array/

class Solution {
    fun numberOfArrays(s: String, k: Int): Int {
        val mod = 1_000_000_007
        val n = s.length
        val dp = IntArray(n + 1)
        dp[n] = 1
        for (i in n - 1 downTo 0) {
            if (s[i] == '0') continue
            var value = 0L
            for (j in i until n) {
                value = value * 10 + (s[j] - '0')
                if (value > k) break
                dp[i] = (dp[i] + dp[j + 1]) % mod
            }
        }
        return dp[0]
    }
}
"""

solutions["1417_reformat_the_string"] = r"""// LeetCode 1417 - Reformat The String
// https://leetcode.com/problems/reformat-the-string/

class Solution {
    fun reformat(s: String): String {
        val letters = ArrayList<Char>()
        val digits = ArrayList<Char>()
        for (c in s) {
            if (c.isLetter()) letters.add(c) else digits.add(c)
        }
        if (kotlin.math.abs(letters.size - digits.size) > 1) return ""
        var a = letters
        var b = digits
        if (b.size >= a.size) {
            a = digits
            b = letters
        }
        val answer = StringBuilder()
        for (i in a.indices) {
            answer.append(a[i])
            if (i < b.size) answer.append(b[i])
        }
        return answer.toString()
    }
}
"""

solutions["1418_display_table_of_food_orders_in_a_restaurant"] = r"""// LeetCode 1418 - Display Table of Food Orders in a Restaurant
// https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

class Solution {
    fun displayTable(orders: List<List<String>>): List<List<String>> {
        val foods = sortedSetOf<String>()
        val tables = sortedSetOf<Int>()
        val counts = HashMap<Pair<Int, String>, Int>()
        for (order in orders) {
            val table = order[1].toInt()
            val food = order[2]
            foods.add(food)
            tables.add(table)
            val key = table to food
            counts[key] = counts.getOrDefault(key, 0) + 1
        }
        val foodList = foods.toList()
        val result = ArrayList<List<String>>()
        result.add(listOf("Table") + foodList)
        for (table in tables) {
            val row = ArrayList<String>()
            row.add(table.toString())
            for (food in foodList) {
                row.add(counts.getOrDefault(table to food, 0).toString())
            }
            result.add(row)
        }
        return result
    }
}
"""

solutions["1419_minimum_number_of_frogs_croaking"] = r"""// LeetCode 1419 - Minimum Number of Frogs Croaking
// https://leetcode.com/problems/minimum-number-of-frogs-croaking/

class Solution {
    fun minNumberOfFrogs(croakOfFrogs: String): Int {
        val order = hashMapOf('c' to 0, 'r' to 1, 'o' to 2, 'a' to 3, 'k' to 4)
        val counts = IntArray(5)
        var active = 0
        var answer = 0
        for (char in croakOfFrogs) {
            val i = order[char] ?: return -1
            if (i > 0 && counts[i - 1] == 0) return -1
            if (i > 0) counts[i - 1]--
            counts[i]++
            if (i == 0) {
                active++
                answer = maxOf(answer, active)
            } else if (i == 4) {
                counts[4]--
                active--
            }
        }
        return if (active == 0) answer else -1
    }
}
"""

solutions["1420_build_array_where_you_can_find_the_maximum_exactly_k_comparisons"] = r"""// LeetCode 1420 - Build Array Where You Can Find The Maximum Exactly K Comparisons
// https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/

class Solution {
    fun numOfArrays(n: Int, m: Int, k: Int): Int {
        val mod = 1_000_000_007
        var dp = Array(k + 1) { IntArray(m + 1) }
        for (maximum in 1..m) dp[1][maximum] = 1
        for (len in 1 until n) {
            val nxt = Array(k + 1) { IntArray(m + 1) }
            for (cost in 1..k) {
                var prefix = 0
                for (maximum in 1..m) {
                    prefix = (prefix + dp[cost - 1][maximum - 1]) % mod
                    nxt[cost][maximum] = ((maximum.toLong() * dp[cost][maximum] + prefix) % mod).toInt()
                }
            }
            dp = nxt
        }
        var answer = 0
        for (v in dp[k]) answer = (answer + v) % mod
        return answer
    }
}
"""

solutions["1422_maximum_score_after_splitting_a_string"] = r"""// LeetCode 1422 - Maximum Score After Splitting a String
// https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution {
    fun maxScore(s: String): Int {
        var ones = s.count { it == '1' }
        var leftZeros = 0
        var answer = 0
        for (i in 0 until s.length - 1) {
            if (s[i] == '0') leftZeros++ else ones--
            answer = maxOf(answer, leftZeros + ones)
        }
        return answer
    }
}
"""

solutions["1423_maximum_points_you_can_obtain_from_cards"] = r"""// LeetCode 1423 - Maximum Points You Can Obtain from Cards
// https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution {
    fun maxScore(cardPoints: IntArray, k: Int): Int {
        val n = cardPoints.size
        if (k == n) return cardPoints.sum()
        val window = n - k
        var current = 0
        for (i in 0 until window) current += cardPoints[i]
        var smallest = current
        for (i in window until n) {
            current += cardPoints[i] - cardPoints[i - window]
            smallest = minOf(smallest, current)
        }
        var total = 0
        for (v in cardPoints) total += v
        return total - smallest
    }
}
"""

solutions["1424_diagonal_traverse_ii"] = r"""// LeetCode 1424 - Diagonal Traverse II
// https://leetcode.com/problems/diagonal-traverse-ii/

class Solution {
    fun findDiagonalOrder(nums: List<List<Int>>): IntArray {
        val diagonals = HashMap<Int, ArrayList<Int>>()
        for (row in nums.indices) {
            for (col in nums[row].indices) {
                diagonals.getOrPut(row + col) { ArrayList() }.add(nums[row][col])
            }
        }
        val answer = ArrayList<Int>()
        for (key in diagonals.keys.sorted()) {
            val diag = diagonals[key]!!
            for (i in diag.size - 1 downTo 0) answer.add(diag[i])
        }
        return answer.toIntArray()
    }
}
"""

solutions["1425_constrained_subsequence_sum"] = r"""// LeetCode 1425 - Constrained Subsequence Sum
// https://leetcode.com/problems/constrained-subsequence-sum/

import java.util.ArrayDeque

class Solution {
    fun constrainedSubsetSum(nums: IntArray, k: Int): Int {
        val queue = ArrayDeque<Int>()
        val best = nums.copyOf()
        for (i in nums.indices) {
            while (queue.isNotEmpty() && queue.first() < i - k) queue.removeFirst()
            best[i] = nums[i] + maxOf(0, if (queue.isEmpty()) 0 else best[queue.first()])
            while (queue.isNotEmpty() && best[queue.last()] <= best[i]) queue.removeLast()
            queue.addLast(i)
        }
        return best.maxOrNull() ?: 0
    }
}
"""


def main() -> None:
    for folder, content in solutions.items():
        path = ROOT / folder / "solution.kt"
        path.write_text(content.rstrip() + "\n", encoding="utf-8")
        print(f"wrote {folder}")
    print(f"total={len(solutions)}")


if __name__ == "__main__":
    main()
