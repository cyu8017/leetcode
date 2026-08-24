#!/usr/bin/env python3
"""Write Scala solutions for batch_12 folders 2869-2911."""
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["2869_minimum_operations_to_collect_elements"] = r'''// LeetCode 2869 - Minimum Operations to Collect Elements
// https://leetcode.com/problems/minimum-operations-to-collect-elements/

object Solution {
  def minOperations(nums: Array[Int], k: Int): Int = {
    val need = scala.collection.mutable.Set((1 to k): _*)
    for (i <- nums.indices.reverse) {
      need.remove(nums(i))
      if (need.isEmpty) return nums.length - i
    }
    nums.length
  }
}
'''

FILES["2870_minimum_number_of_operations_to_make_array_empty"] = r'''// LeetCode 2870 - Minimum Number of Operations to Make Array Empty
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

object Solution {
  def minOperations(nums: Array[Int]): Int = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    nums.foreach(v => freq(v) = freq.getOrElse(v, 0) + 1)
    var ans = 0
    freq.values.foreach { c =>
      if (c == 1) return -1
      ans += (c + 2) / 3
    }
    ans
  }
}
'''

FILES["2871_split_array_into_maximum_number_of_subarrays"] = r'''// LeetCode 2871 - Split Array Into Maximum Number of Subarrays
// https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/

object Solution {
  def maxSubarrays(nums: Array[Int]): Int = {
    var ans = 0
    var cur = -1
    nums.foreach { v =>
      if (cur == -1) cur = v
      else cur &= v
      if (cur == 0) {
        ans += 1
        cur = -1
      }
    }
    if (ans == 0) 1 else ans
  }
}
'''

FILES["2872_maximum_number_of_k_divisible_components"] = r'''// LeetCode 2872 - Maximum Number of K-Divisible Components
// https://leetcode.com/problems/maximum-number-of-k-divisible-components/

object Solution {
  private var g: Array[scala.collection.mutable.ArrayBuffer[Int]] = _
  private var values: Array[Int] = _
  private var k: Int = _
  private var ans: Int = _

  def maxKDivisibleComponents(n: Int, edges: Array[Array[Int]], values: Array[Int], k: Int): Int = {
    this.values = values
    this.k = k
    g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    ans = 0
    dfs(0, -1)
    ans
  }

  private def dfs(u: Int, p: Int): Int = {
    var sum = values(u) % k
    g(u).foreach { v =>
      if (v != p) sum = (sum + dfs(v, u)) % k
    }
    if (sum == 0) ans += 1
    sum
  }
}
'''

FILES["2873_maximum_value_of_an_ordered_triplet_i"] = r'''// LeetCode 2873 - Maximum Value of an Ordered Triplet I
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

object Solution {
  def maximumTripletValue(nums: Array[Int]): Long = {
    val n = nums.length
    var ans = 0L
    for (i <- 0 until n; j <- i + 1 until n; k <- j + 1 until n) {
      val cand = 1L * (nums(i) - nums(j)) * nums(k)
      if (cand > ans) ans = cand
    }
    ans
  }
}
'''

FILES["2874_maximum_value_of_an_ordered_triplet_ii"] = r'''// LeetCode 2874 - Maximum Value of an Ordered Triplet II
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

object Solution {
  def maximumTripletValue(nums: Array[Int]): Long = {
    var ans = 0L
    var maxI = 0L
    var maxDiff = 0L
    nums.foreach { v =>
      val value = v.toLong
      if (maxDiff * value > ans) ans = maxDiff * value
      if (maxI - value > maxDiff) maxDiff = maxI - value
      if (value > maxI) maxI = value
    }
    ans
  }
}
'''

FILES["2875_minimum_size_subarray_in_infinite_array"] = r'''// LeetCode 2875 - Minimum Size Subarray in Infinite Array
// https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

object Solution {
  def minSizeSubarray(nums: Array[Int], target: Int): Int = {
    val n = nums.length
    var total = 0L
    nums.foreach(v => total += v)
    var ans = 1 << 30
    if (total > 0) {
      val loops = (target / total).toInt
      val remain = (target % total).toInt
      if (remain == 0) return loops * n
      val arr = nums ++ nums
      var left = 0
      var sum = 0
      var best = 1 << 30
      for (right <- arr.indices) {
        sum += arr(right)
        while (sum > remain && left <= right) {
          sum -= arr(left)
          left += 1
        }
        if (sum == remain && right - left + 1 < best) best = right - left + 1
      }
      if (best < (1 << 30)) ans = loops * n + best
    }
    if (ans == (1 << 30)) -1 else ans
  }
}
'''

FILES["2876_count_visited_nodes_in_a_directed_graph"] = r'''// LeetCode 2876 - Count Visited Nodes in a Directed Graph
// https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/

object Solution {
  private var edges: Array[Int] = _
  private var ans: Array[Int] = _
  private var state: Array[Int] = _
  private var stack: scala.collection.mutable.ArrayBuffer[Int] = _

  def countVisitedNodes(edgesList: Array[Int]): Array[Int] = {
    val n = edgesList.length
    edges = edgesList
    ans = Array.fill(n)(0)
    state = Array.fill(n)(0)
    stack = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (i <- 0 until n if state(i) == 0) dfs(i)
    ans
  }

  private def dfs(u: Int): Unit = {
    state(u) = 1
    stack += u
    val v = edges(u)
    if (state(v) == 0) dfs(v)
    else if (state(v) == 1) {
      var idx = stack.length - 1
      while (stack(idx) != v) idx -= 1
      val cyc = stack.length - idx
      for (i <- idx until stack.length) ans(stack(i)) = cyc
    }
    if (ans(u) == 0) ans(u) = ans(edges(u)) + 1
    state(u) = 2
    stack.remove(stack.length - 1)
  }
}
'''

FILES["2877_create_a_dataframe_from_list"] = r'''// LeetCode 2877 - Create a DataFrame from List
// https://leetcode.com/problems/create-a-dataframe-from-list/

object Solution {
  def createDataframe(student_data: Array[Array[Int]]): Array[Map[String, Int]] = {
    student_data.map { row =>
      Map("student_id" -> row(0), "age" -> row(1))
    }
  }
}
'''

FILES["2878_get_the_size_of_a_dataframe"] = r'''// LeetCode 2878 - Get the Size of a DataFrame
// https://leetcode.com/problems/get-the-size-of-a-dataframe/

object Solution {
  def getDataframeSize(players: Any): Array[Int] = {
    players match {
      case null => Array(0, 0)
      case rows: Array[_] if rows.isEmpty => Array(0, 0)
      case rows: Array[Array[Int]] => Array(rows.length, rows.headOption.map(_.length).getOrElse(0))
      case rows: Seq[_] if rows.isEmpty => Array(0, 0)
      case rows: Seq[_] =>
        val cols = rows.head match {
          case first: Seq[_] => first.length
          case first: Map[_, _] => first.size
          case first: Array[_] => first.length
          case _ => 0
        }
        Array(rows.length, cols)
      case _ => Array(0, 0)
    }
  }
}
'''

FILES["2879_display_the_first_three_rows"] = r'''// LeetCode 2879 - Display the First Three Rows
// https://leetcode.com/problems/display-the-first-three-rows/

object Solution {
  def selectFirstRows(employees: Array[Any]): Array[Any] = employees.take(3)
}
'''

FILES["2880_select_data"] = r'''// LeetCode 2880 - Select Data
// https://leetcode.com/problems/select-data/

object Solution {
  def selectData(students: Array[Any]): Array[Map[String, Any]] = {
    students.flatMap {
      case r: Seq[_] if r.head == 101 => Some(Map("name" -> r(1), "age" -> r(2)))
      case r: Array[_] if r.head == 101 => Some(Map("name" -> r(1), "age" -> r(2)))
      case r: Map[String, Any] @unchecked if r.getOrElse("student_id", -1) == 101 =>
        Some(Map("name" -> r("name"), "age" -> r("age")))
      case _ => None
    }
  }
}
'''

FILES["2881_create_a_new_column"] = r'''// LeetCode 2881 - Create a New Column
// https://leetcode.com/problems/create-a-new-column/

object Solution {
  def createBonusColumn(employees: Array[Any]): Array[Map[String, Any]] = {
    employees.map {
      case r: Seq[_] =>
        val salary = r(1).asInstanceOf[Int]
        Map("name" -> r(0), "salary" -> salary, "bonus" -> (salary * 2))
      case r: Array[_] =>
        val salary = r(1).asInstanceOf[Int]
        Map("name" -> r(0), "salary" -> salary, "bonus" -> (salary * 2))
      case r: Map[String, Any] @unchecked =>
        val salary = r("salary").asInstanceOf[Int]
        r + ("bonus" -> (salary * 2))
    }
  }
}
'''

FILES["2882_drop_duplicate_rows"] = r'''// LeetCode 2882 - Drop Duplicate Rows
// https://leetcode.com/problems/drop-duplicate-rows/

object Solution {
  def dropDuplicateEmails(customers: Array[Any]): Array[Any] = {
    val seen = scala.collection.mutable.Set.empty[Any]
    customers.filter { r =>
      val email = r match {
        case row: Seq[_] => row(2)
        case row: Array[_] => row(2)
        case row: Map[String, Any] @unchecked => row("email")
      }
      if (seen.contains(email)) false
      else {
        seen += email
        true
      }
    }
  }
}
'''

FILES["2883_drop_missing_data"] = r'''// LeetCode 2883 - Drop Missing Data
// https://leetcode.com/problems/drop-missing-data/

object Solution {
  def dropMissingData(students: Array[Any]): Array[Any] = {
    students.filter { r =>
      val name = r match {
        case row: Seq[_] => row(1)
        case row: Array[_] => row(1)
        case row: Map[String, Any] @unchecked => row.getOrElse("name", null)
      }
      name != null && name != ""
    }
  }
}
'''

FILES["2884_modify_columns"] = r'''// LeetCode 2884 - Modify Columns
// https://leetcode.com/problems/modify-columns/

object Solution {
  def modifySalaryColumn(employees: Array[Any]): Array[Any] = {
    employees.map {
      case r: Seq[_] => Seq(r(0), r(1).asInstanceOf[Int] * 2)
      case r: Array[_] => Array(r(0), r(1).asInstanceOf[Int] * 2)
      case r: Map[String, Any] @unchecked =>
        r + ("salary" -> (r("salary").asInstanceOf[Int] * 2))
    }
  }
}
'''

FILES["2885_rename_columns"] = r'''// LeetCode 2885 - Rename Columns
// https://leetcode.com/problems/rename-columns/

object Solution {
  def renameColumns(students: Array[Any]): Array[Map[String, Any]] = {
    students.map {
      case r: Seq[_] =>
        Map("student_id" -> r(0), "first_name" -> r(1), "last_name" -> r(2), "age_in_years" -> r(3))
      case r: Array[_] =>
        Map("student_id" -> r(0), "first_name" -> r(1), "last_name" -> r(2), "age_in_years" -> r(3))
      case r: Map[String, Any] @unchecked =>
        Map(
          "student_id" -> r("id"),
          "first_name" -> r("first"),
          "last_name" -> r("last"),
          "age_in_years" -> r("age")
        )
    }
  }
}
'''

FILES["2886_change_data_type"] = r'''// LeetCode 2886 - Change Data Type
// https://leetcode.com/problems/change-data-type/

object Solution {
  def changeDatatype(students: Array[Any]): Array[Any] = {
    students.map {
      case r: Seq[_] => Seq(r(0), r(1), r(2), r(3).toString.toInt)
      case r: Array[_] => Array(r(0), r(1), r(2), r(3).toString.toInt)
      case r: Map[String, Any] @unchecked =>
        r + ("grade" -> r("grade").toString.toInt)
    }
  }
}
'''

FILES["2887_fill_missing_data"] = r'''// LeetCode 2887 - Fill Missing Data
// https://leetcode.com/problems/fill-missing-data/

object Solution {
  def fillMissingValues(products: Array[Any]): Array[Any] = {
    products.map {
      case r: Seq[_] => Seq(r(0), if (r(1) == null) 0 else r(1), r(2))
      case r: Array[_] => Array(r(0), if (r(1) == null) 0 else r(1), r(2))
      case r: Map[String, Any] @unchecked =>
        r + ("quantity" -> (if (r.getOrElse("quantity", null) == null) 0 else r("quantity")))
    }
  }
}
'''

FILES["2888_reshape_data_concatenate"] = r'''// LeetCode 2888 - Reshape Data: Concatenate
// https://leetcode.com/problems/reshape-data-concatenate/

object Solution {
  def concatenateTables(df1: Array[Any], df2: Array[Any]): Array[Any] = df1 ++ df2
}
'''

FILES["2889_reshape_data_pivot"] = r'''// LeetCode 2889 - Reshape Data: Pivot
// https://leetcode.com/problems/reshape-data-pivot/

object Solution {
  def pivotTable(weather: Array[Any]): Array[Map[String, Any]] = {
    val months = scala.collection.mutable.ArrayBuffer.empty[Any]
    val byMonth = scala.collection.mutable.LinkedHashMap.empty[Any, scala.collection.mutable.Map[Any, Any]]
    weather.foreach {
      case r: Seq[_] => add(months, byMonth, r(0), r(1), r(2))
      case r: Array[_] => add(months, byMonth, r(0), r(1), r(2))
      case r: Map[String, Any] @unchecked =>
        add(months, byMonth, r("city"), r("month"), r("temperature"))
    }
    months.map { month =>
      Map[String, Any]("month" -> month) ++ byMonth(month).map { case (k, v) => k.toString -> v }
    }.toArray
  }

  private def add(
      months: scala.collection.mutable.ArrayBuffer[Any],
      byMonth: scala.collection.mutable.LinkedHashMap[Any, scala.collection.mutable.Map[Any, Any]],
      city: Any,
      month: Any,
      temperature: Any
  ): Unit = {
    if (!byMonth.contains(month)) {
      byMonth(month) = scala.collection.mutable.Map.empty[Any, Any]
      months += month
    }
    byMonth(month)(city) = temperature
  }
}
'''

FILES["2890_reshape_data_melt"] = r'''// LeetCode 2890 - Reshape Data: Melt
// https://leetcode.com/problems/reshape-data-melt/

object Solution {
  def meltTable(report: Array[Any]): Array[Map[String, Any]] = {
    report.flatMap {
      case r: Seq[_] =>
        (1 to 4).map { q =>
          Map("product" -> r(0), "quarter" -> s"quarter_$q", "sales" -> r(q))
        }
      case r: Array[_] =>
        (1 to 4).map { q =>
          Map("product" -> r(0), "quarter" -> s"quarter_$q", "sales" -> r(q))
        }
      case r: Map[String, Any] @unchecked =>
        Seq("quarter_1", "quarter_2", "quarter_3", "quarter_4").map { q =>
          Map("product" -> r("product"), "quarter" -> q, "sales" -> r(q))
        }
    }
  }
}
'''

FILES["2891_method_chaining"] = r'''// LeetCode 2891 - Method Chaining
// https://leetcode.com/problems/method-chaining/

object Solution {
  def findHeavyAnimals(animals: Array[Any]): Array[Map[String, Any]] = {
    def weight(r: Any): Int = r match {
      case row: Seq[_] => row(3).asInstanceOf[Int]
      case row: Array[_] => row(3).asInstanceOf[Int]
      case row: Map[String, Any] @unchecked => row("weight").asInstanceOf[Int]
    }
    def name(r: Any): Any = r match {
      case row: Seq[_] => row(0)
      case row: Array[_] => row(0)
      case row: Map[String, Any] @unchecked => row("name")
    }
    animals.filter(weight(_) > 100).sortBy(r => -weight(r)).map(r => Map("name" -> name(r)))
  }
}
'''

FILES["2892_minimizing_array_after_replacing_pairs_with_their_product"] = r'''// LeetCode 2892 - Minimizing Array After Replacing Pairs With Their Product
// https://leetcode.com/problems/minimizing-array-after-replacing-pairs-with-their-product/

object Solution {
  def minArrayLength(nums: Array[Int], k: Int): Int = {
    if (nums.isEmpty) return 0
    var ans = 1
    var prod = nums(0).toLong
    for (i <- 1 until nums.length) {
      if (prod <= k && nums(i) <= k && (nums(i) == 0 || prod <= k / nums(i))) {
        prod *= nums(i)
      } else {
        ans += 1
        prod = nums(i)
      }
    }
    ans
  }
}
'''

FILES["2894_divisible_and_non_divisible_sums_difference"] = r'''// LeetCode 2894 - Divisible and Non-divisible Sums Difference
// https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

object Solution {
  def differenceOfSums(n: Int, m: Int): Int = {
    var num1 = 0
    var num2 = 0
    for (i <- 1 to n) {
      if (i % m == 0) num2 += i
      else num1 += i
    }
    num1 - num2
  }
}
'''

FILES["2895_minimum_processing_time"] = r'''// LeetCode 2895 - Minimum Processing Time
// https://leetcode.com/problems/minimum-processing-time/

object Solution {
  def minProcessingTime(processorTime: Array[Int], tasks: Array[Int]): Int = {
    val processors = processorTime.sorted
    val t = tasks.sorted(Ordering[Int].reverse)
    var ans = 0
    for (i <- processors.indices) {
      val fin = processors(i) + t(i * 4)
      if (fin > ans) ans = fin
    }
    ans
  }
}
'''

FILES["2896_apply_operations_to_make_two_strings_equal"] = r'''// LeetCode 2896 - Apply Operations to Make Two Strings Equal
// https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/

object Solution {
  def minOperations(s1: String, s2: String, x: Int): Int = {
    val diff = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (i <- s1.indices if s1.charAt(i) != s2.charAt(i)) diff += i
    val m = diff.length
    if (m % 2 == 1) return -1
    if (m == 0) return 0
    val dp2 = Array.fill(m + 1)(1 << 30)
    dp2(0) = 0
    for (i <- 0 until m) {
      if (dp2(i) < (1 << 30) && i + 1 < m) {
        var cand = diff(i + 1) - diff(i)
        if (cand > x) cand = x
        if (dp2(i) + cand < dp2(i + 2)) dp2(i + 2) = dp2(i) + cand
      }
    }
    if (dp2(m) >= (1 << 30)) -1 else dp2(m)
  }
}
'''

FILES["2897_apply_operations_on_array_to_maximize_sum_of_squares"] = r'''// LeetCode 2897 - Apply Operations on Array to Maximize Sum of Squares
// https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/

object Solution {
  def maxSum(nums: Array[Int], k: Int): Int = {
    val mod = 1000000007
    val cnt = Array.fill(32)(0)
    nums.foreach { v =>
      for (b <- 0 until 32 if (v & (1 << b)) != 0) cnt(b) += 1
    }
    var ans = 0
    for (_ <- 0 until k) {
      var cur = 0
      for (b <- 0 until 32 if cnt(b) > 0) {
        cur |= 1 << b
        cnt(b) -= 1
      }
      ans = ((ans + 1L * (cur % mod) * (cur % mod) % mod) % mod).toInt
    }
    ans
  }
}
'''

FILES["2898_maximum_linear_stock_score"] = r'''// LeetCode 2898 - Maximum Linear Stock Score
// https://leetcode.com/problems/maximum-linear-stock-score/

object Solution {
  def maxScore(prices: Array[Int]): Long = {
    val best = scala.collection.mutable.Map.empty[Int, Long]
    var ans = 0L
    for (i <- prices.indices) {
      val key = prices(i) - (i + 1)
      val cand = best.getOrElse(key, 0L) + prices(i)
      if (cand > best.getOrElse(key, 0L)) best(key) = cand
      if (best(key) > ans) ans = best(key)
    }
    ans
  }
}
'''

FILES["2899_last_visited_integers"] = r'''// LeetCode 2899 - Last Visited Integers
// https://leetcode.com/problems/last-visited-integers/

object Solution {
  def lastVisitedIntegers(nums: Array[Int]): Array[Int] = {
    val seen = scala.collection.mutable.ArrayBuffer.empty[Int]
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    var k = 0
    nums.foreach { v =>
      if (v != -1) {
        seen += v
        k = 0
      } else {
        k += 1
        if (k > seen.length) ans += -1
        else ans += seen(seen.length - k)
      }
    }
    ans.toArray
  }
}
'''

FILES["2900_longest_unequal_adjacent_groups_subsequence_i"] = r'''// LeetCode 2900 - Longest Unequal Adjacent Groups Subsequence I
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

object Solution {
  def getLongestSubsequence(words: Array[String], groups: Array[Int]): Array[String] = {
    val ans = scala.collection.mutable.ArrayBuffer(words(0))
    var last = groups(0)
    for (i <- 1 until words.length if groups(i) != last) {
      ans += words(i)
      last = groups(i)
    }
    ans.toArray
  }
}
'''

FILES["2901_longest_unequal_adjacent_groups_subsequence_ii"] = r'''// LeetCode 2901 - Longest Unequal Adjacent Groups Subsequence II
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

object Solution {
  def getWordsInLongestSubsequence(words: Array[String], groups: Array[Int]): Array[String] = {
    val n = words.length
    val dp = Array.fill(n)(1)
    val prev = Array.fill(n)(-1)
    var best = 1
    var bestI = 0
    for (i <- 0 until n) {
      for (j <- 0 until i) {
        if (groups(i) != groups(j) && hamming(words(i), words(j)) == 1 && dp(j) + 1 > dp(i)) {
          dp(i) = dp(j) + 1
          prev(i) = j
        }
      }
      if (dp(i) > best) {
        best = dp(i)
        bestI = i
      }
    }
    val path = scala.collection.mutable.ArrayBuffer.empty[String]
    var i = bestI
    while (i != -1) {
      path += words(i)
      i = prev(i)
    }
    path.reverse.toArray
  }

  private def hamming(a: String, b: String): Int = {
    if (a.length != b.length) return 100
    var d = 0
    for (i <- a.indices if a.charAt(i) != b.charAt(i)) d += 1
    d
  }
}
'''

FILES["2902_count_of_sub_multisets_with_bounded_sum"] = r'''// LeetCode 2902 - Count of Sub-Multisets With Bounded Sum
// https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/

object Solution {
  def countSubMultisets(nums: Array[Int], l: Int, r0: Int): Int = {
    val mod = 1000000007
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    var total = 0
    nums.foreach { v =>
      freq(v) = freq.getOrElse(v, 0) + 1
      total += v
    }
    if (total < l) return 0
    var r = r0
    if (r > total) r = total
    var dp = Array.fill(r + 1)(0)
    dp(0) = 1
    val zeros = freq.getOrElse(0, 0)
    freq.remove(0)
    freq.foreach { case (v, c) =>
      val ndp = Array.fill(r + 1)(0)
      for (sum <- 0 to r if dp(sum) != 0) {
        var k = 0
        while (k <= c && sum + k * v <= r) {
          ndp(sum + k * v) = (ndp(sum + k * v) + dp(sum)) % mod
          k += 1
        }
      }
      dp = ndp
    }
    var ans = 0
    for (s <- l to r) ans = (ans + dp(s)) % mod
    (1L * ans * (zeros + 1) % mod).toInt
  }
}
'''

FILES["2903_find_indices_with_index_and_value_difference_i"] = r'''// LeetCode 2903 - Find Indices With Index and Value Difference I
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

object Solution {
  def findIndices(nums: Array[Int], indexDifference: Int, valueDifference: Int): Array[Int] = {
    val n = nums.length
    for (i <- 0 until n; j <- i until n) {
      val di = math.abs(j - i)
      val dv = math.abs(nums(i) - nums(j))
      if (di >= indexDifference && dv >= valueDifference) return Array(i, j)
    }
    Array(-1, -1)
  }
}
'''

FILES["2904_shortest_and_lexicographically_smallest_beautiful_string"] = r'''// LeetCode 2904 - Shortest and Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

object Solution {
  def shortestBeautifulSubstring(s: String, k: Int): String = {
    var ans = ""
    val n = s.length
    for (i <- 0 until n) {
      var ones = 0
      var j = i
      var done = false
      while (j < n && !done) {
        if (s.charAt(j) == '1') ones += 1
        if (ones == k) {
          val cand = s.substring(i, j + 1)
          if (ans.isEmpty || cand.length < ans.length || (cand.length == ans.length && cand < ans))
            ans = cand
          done = true
        } else if (ones > k) done = true
        j += 1
      }
    }
    ans
  }
}
'''

FILES["2905_find_indices_with_index_and_value_difference_ii"] = r'''// LeetCode 2905 - Find Indices With Index and Value Difference II
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

object Solution {
  def findIndices(nums: Array[Int], indexDifference: Int, valueDifference: Int): Array[Int] = {
    val n = nums.length
    var minIdx = 0
    var maxIdx = 0
    for (j <- indexDifference until n) {
      val i = j - indexDifference
      if (nums(i) < nums(minIdx)) minIdx = i
      if (nums(i) > nums(maxIdx)) maxIdx = i
      if (nums(j) - nums(minIdx) >= valueDifference) return Array(minIdx, j)
      if (nums(maxIdx) - nums(j) >= valueDifference) return Array(maxIdx, j)
    }
    Array(-1, -1)
  }
}
'''

FILES["2906_construct_product_matrix"] = r'''// LeetCode 2906 - Construct Product Matrix
// https://leetcode.com/problems/construct-product-matrix/

object Solution {
  def constructProductMatrix(grid: Array[Array[Int]]): Array[Array[Int]] = {
    val mod = 12345
    val m = grid.length
    val n = grid(0).length
    val ans = Array.ofDim[Int](m, n)
    var pref = 1
    for (i <- 0 until m; j <- 0 until n) {
      ans(i)(j) = pref
      pref = (1L * pref * (grid(i)(j) % mod) % mod).toInt
    }
    var suf = 1
    for (i <- m - 1 to 0 by -1; j <- n - 1 to 0 by -1) {
      ans(i)(j) = (1L * ans(i)(j) * suf % mod).toInt
      suf = (1L * suf * (grid(i)(j) % mod) % mod).toInt
    }
    ans
  }
}
'''

FILES["2907_maximum_profitable_triplets_with_increasing_prices_i"] = r'''// LeetCode 2907 - Maximum Profitable Triplets With Increasing Prices I
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-i/

object Solution {
  def maxProfit(prices: Array[Int], profits: Array[Int]): Int = {
    val n = prices.length
    var ans = -1
    for (j <- 0 until n) {
      var bestL = -1
      var bestR = -1
      for (i <- 0 until j if prices(i) < prices(j) && profits(i) > bestL) bestL = profits(i)
      for (k <- j + 1 until n if prices(k) > prices(j) && profits(k) > bestR) bestR = profits(k)
      if (bestL >= 0 && bestR >= 0) {
        val cand = bestL + profits(j) + bestR
        if (cand > ans) ans = cand
      }
    }
    ans
  }
}
'''

FILES["2908_minimum_sum_of_mountain_triplets_i"] = r'''// LeetCode 2908 - Minimum Sum of Mountain Triplets I
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/

object Solution {
  def minimumSum(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 1 << 30
    for (j <- 1 until n - 1) {
      var left = 1 << 30
      var right = 1 << 30
      for (i <- 0 until j if nums(i) < nums(j) && nums(i) < left) left = nums(i)
      for (k <- j + 1 until n if nums(k) < nums(j) && nums(k) < right) right = nums(k)
      if (left < (1 << 30) && right < (1 << 30)) {
        val cand = left + nums(j) + right
        if (cand < ans) ans = cand
      }
    }
    if (ans == (1 << 30)) -1 else ans
  }
}
'''

FILES["2909_minimum_sum_of_mountain_triplets_ii"] = r'''// LeetCode 2909 - Minimum Sum of Mountain Triplets II
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/

object Solution {
  def minimumSum(nums: Array[Int]): Int = {
    val n = nums.length
    val left = Array.fill(n)(0)
    val right = Array.fill(n)(0)
    var mn = 1 << 30
    for (i <- 0 until n) {
      left(i) = mn
      if (nums(i) < mn) mn = nums(i)
    }
    mn = 1 << 30
    for (i <- n - 1 to 0 by -1) {
      right(i) = mn
      if (nums(i) < mn) mn = nums(i)
    }
    var ans = 1 << 30
    for (j <- 1 until n - 1) {
      if (left(j) < nums(j) && right(j) < nums(j)) {
        val cand = left(j) + nums(j) + right(j)
        if (cand < ans) ans = cand
      }
    }
    if (ans == (1 << 30)) -1 else ans
  }
}
'''

FILES["2910_minimum_number_of_groups_to_create_a_valid_assignment"] = r'''// LeetCode 2910 - Minimum Number of Groups to Create a Valid Assignment
// https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/

object Solution {
  def minGroupsForValidAssignment(balls: Array[Int]): Int = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    balls.foreach(b => freq(b) = freq.getOrElse(b, 0) + 1)
    val counts = freq.values.toArray
    val minF = counts.min
    for (size <- minF to 1 by -1) {
      var ok = true
      var groups = 0
      counts.foreach { c =>
        if (ok) {
          val rem = c % (size + 1)
          val g2 = c / (size + 1)
          if (rem == 0) groups += g2
          else if (size - rem <= g2) groups += g2 + 1
          else ok = false
        }
      }
      if (ok) return groups
    }
    balls.length
  }
}
'''

FILES["2911_minimum_changes_to_make_k_semi_palindromes"] = r'''// LeetCode 2911 - Minimum Changes to Make K Semi-palindromes
// https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

object Solution {
  private var s: String = _

  def minimumChanges(s: String, k: Int): Int = {
    this.s = s
    val n = s.length
    val cost = Array.fill(n, n)(1 << 20)
    for (i <- 0 until n; j <- i + 1 until n) cost(i)(j) = semiCost(i, j)
    val dp = Array.fill(k + 1, n + 1)(1 << 20)
    dp(0)(0) = 0
    for (p <- 1 to k; i <- 1 to n; t <- 0 until i - 1) {
      val cand = dp(p - 1)(t) + cost(t)(i - 1)
      if (cand < dp(p)(i)) dp(p)(i) = cand
    }
    dp(k)(n)
  }

  private def semiCost(l: Int, r: Int): Int = {
    val length = r - l + 1
    var best = 1 << 20
    for (d <- 1 until length if length % d == 0) {
      var chg = 0
      for (start <- 0 until d) {
        val chars = new StringBuilder
        var i = l + start
        while (i <= r) {
          chars.append(s.charAt(i))
          i += d
        }
        var a = 0
        var b = chars.length - 1
        while (a < b) {
          if (chars.charAt(a) != chars.charAt(b)) chg += 1
          a += 1
          b -= 1
        }
      }
      if (chg < best) best = chg
    }
    best
  }
}
'''

def main() -> None:
    written = 0
    for folder, content in FILES.items():
        path = ROOT / folder / "Solution.scala"
        path.write_text(content, encoding="utf-8", newline="\n")
        if path.read_bytes().startswith(b"\xef\xbb\xbf"):
            raise SystemExit(f"BOM in {path}")
        written += 1
        print(f"wrote {folder}")
    print(f"written={written}")


if __name__ == "__main__":
    main()
