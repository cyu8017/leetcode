#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("2885_rename_columns", r'''
# LeetCode 2885 - Rename Columns
# https://leetcode.com/problems/rename-columns/

# @param {Object[]} students
# @return {Object[]}
def rename_columns(students)
  students.map do |r|
    if r.is_a?(Array)
      {
        "student_id" => r[0],
        "first_name" => r[1],
        "last_name" => r[2],
        "age_in_years" => r[3]
      }
    else
      {
        "student_id" => r["id"],
        "first_name" => r["first"],
        "last_name" => r["last"],
        "age_in_years" => r["age"]
      }
    end
  end
end
''')

add("2886_change_data_type", r'''
# LeetCode 2886 - Change Data Type
# https://leetcode.com/problems/change-data-type/

# @param {Object[]} students
# @return {Object[]}
def change_datatype(students)
  students.map do |r|
    if r.is_a?(Array)
      [r[0], r[1], r[2], r[3].to_i]
    else
      row = r.dup
      row["grade"] = r["grade"].to_i
      row
    end
  end
end
''')

add("2887_fill_missing_data", r'''
# LeetCode 2887 - Fill Missing Data
# https://leetcode.com/problems/fill-missing-data/

# @param {Object[]} products
# @return {Object[]}
def fill_missing_values(products)
  products.map do |r|
    if r.is_a?(Array)
      q = r[1]
      [r[0], q.nil? ? 0 : q, r[2]]
    else
      row = r.dup
      row["quantity"] = r["quantity"].nil? ? 0 : r["quantity"]
      row
    end
  end
end
''')

add("2888_reshape_data_concatenate", r'''
# LeetCode 2888 - Reshape Data: Concatenate
# https://leetcode.com/problems/reshape-data-concatenate/

# @param {Object[]} df1
# @param {Object[]} df2
# @return {Object[]}
def concatenate_tables(df1, df2)
  df1 + df2
end
''')

add("2889_reshape_data_pivot", r'''
# LeetCode 2889 - Reshape Data: Pivot
# https://leetcode.com/problems/reshape-data-pivot/

# @param {Object[]} weather
# @return {Object[]}
def pivot_table(weather)
  months = []
  by_month = {}
  weather.each do |r|
    if r.is_a?(Array)
      city, month, temperature = r[0], r[1], r[2]
    else
      city, month, temperature = r["city"], r["month"], r["temperature"]
    end
    unless by_month.key?(month)
      by_month[month] = {}
      months << month
    end
    by_month[month][city] = temperature
  end
  months.map { |month| { "month" => month }.merge(by_month[month]) }
end
''')

add("2890_reshape_data_melt", r'''
# LeetCode 2890 - Reshape Data: Melt
# https://leetcode.com/problems/reshape-data-melt/

# @param {Object[]} report
# @return {Object[]}
def melt_table(report)
  out = []
  report.each do |r|
    if r.is_a?(Array)
      product = r[0]
      (1..4).each do |q|
        out << { "product" => product, "quarter" => "quarter_#{q}", "sales" => r[q] }
      end
    else
      %w[quarter_1 quarter_2 quarter_3 quarter_4].each do |q|
        out << { "product" => r["product"], "quarter" => q, "sales" => r[q] }
      end
    end
  end
  out
end
''')

add("2891_method_chaining", r'''
# LeetCode 2891 - Method Chaining
# https://leetcode.com/problems/method-chaining/

# @param {Object[]} animals
# @return {Object[]}
def find_heavy_animals(animals)
  weight = lambda { |r| r.is_a?(Array) ? r[3] : r["weight"] }
  filtered = animals.select { |r| weight.call(r) > 100 }
  filtered.sort_by! { |r| -weight.call(r) }
  filtered.map { |r| { "name" => r.is_a?(Array) ? r[0] : r["name"] } }
end
''')

add("2892_minimizing_array_after_replacing_pairs_with_their_product", r'''
# LeetCode 2892 - Minimizing Array After Replacing Pairs With Their Product
# https://leetcode.com/problems/minimizing-array-after-replacing-pairs-with-their-product/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_array_length(nums, k)
  return 0 if nums.empty?

  ans = 1
  prod = nums[0]
  (1...nums.length).each do |i|
    if prod <= k && nums[i] <= k && (nums[i] == 0 || prod <= k / nums[i])
      prod *= nums[i]
    else
      ans += 1
      prod = nums[i]
    end
  end
  ans
end
''')

add("2894_divisible_and_non_divisible_sums_difference", r'''
# LeetCode 2894 - Divisible and Non-divisible Sums Difference
# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

# @param {Integer} n
# @param {Integer} m
# @return {Integer}
def difference_of_sums(n, m)
  num1 = num2 = 0
  (1..n).each do |i|
    if i % m == 0
      num2 += i
    else
      num1 += i
    end
  end
  num1 - num2
end
''')

add("2895_minimum_processing_time", r'''
# LeetCode 2895 - Minimum Processing Time
# https://leetcode.com/problems/minimum-processing-time/

# @param {Integer[]} processor_time
# @param {Integer[]} tasks
# @return {Integer}
def min_processing_time(processor_time, tasks)
  processor_time = processor_time.sort
  tasks = tasks.sort.reverse
  ans = 0
  processor_time.each_with_index do |pt, i|
    fin = pt + tasks[i * 4]
    ans = fin if fin > ans
  end
  ans
end
''')

add("2896_apply_operations_to_make_two_strings_equal", r'''
# LeetCode 2896 - Apply Operations to Make Two Strings Equal
# https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/

# @param {String} s1
# @param {String} s2
# @param {Integer} x
# @return {Integer}
def min_operations(s1, s2, x)
  diff = []
  (0...s1.length).each { |i| diff << i if s1[i] != s2[i] }
  m = diff.length
  return -1 if m.odd?
  return 0 if m == 0

  inf = 1 << 30
  dp2 = Array.new(m + 1, inf)
  dp2[0] = 0
  (0...m).each do |i|
    next if dp2[i] >= inf
    next unless i + 1 < m

    cand = diff[i + 1] - diff[i]
    cand = x if cand > x
    dp2[i + 2] = dp2[i] + cand if dp2[i] + cand < dp2[i + 2]
  end
  dp2[m] >= inf ? -1 : dp2[m]
end
''')

add("2897_apply_operations_on_array_to_maximize_sum_of_squares", r'''
# LeetCode 2897 - Apply Operations on Array to Maximize Sum of Squares
# https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_sum(nums, k)
  mod = 1_000_000_007
  cnt = Array.new(32, 0)
  nums.each do |v|
    (0...32).each { |b| cnt[b] += 1 if (v & (1 << b)) != 0 }
  end
  ans = 0
  k.times do
    cur = 0
    (0...32).each do |b|
      if cnt[b] > 0
        cur |= 1 << b
        cnt[b] -= 1
      end
    end
    ans = (ans + ((cur % mod) * (cur % mod)) % mod) % mod
  end
  ans
end
''')

add("2898_maximum_linear_stock_score", r'''
# LeetCode 2898 - Maximum Linear Stock Score
# https://leetcode.com/problems/maximum-linear-stock-score/

# @param {Integer[]} prices
# @return {Integer}
def max_score(prices)
  best = {}
  ans = 0
  prices.each_with_index do |price, i|
    key = price - (i + 1)
    cand = best.fetch(key, 0) + price
    best[key] = cand if cand > best.fetch(key, 0)
    ans = best[key] if best[key] > ans
  end
  ans
end
''')

add("2899_last_visited_integers", r'''
# LeetCode 2899 - Last Visited Integers
# https://leetcode.com/problems/last-visited-integers/

# @param {Integer[]} nums
# @return {Integer[]}
def last_visited_integers(nums)
  seen = []
  ans = []
  k = 0
  nums.each do |v|
    if v != -1
      seen << v
      k = 0
    else
      k += 1
      ans << (k > seen.length ? -1 : seen[-k])
    end
  end
  ans
end
''')

add("2900_longest_unequal_adjacent_groups_subsequence_i", r'''
# LeetCode 2900 - Longest Unequal Adjacent Groups Subsequence I
# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

# @param {String[]} words
# @param {Integer[]} groups
# @return {String[]}
def get_longest_subsequence(words, groups)
  ans = [words[0]]
  last = groups[0]
  (1...words.length).each do |i|
    if groups[i] != last
      ans << words[i]
      last = groups[i]
    end
  end
  ans
end
''')

add("2901_longest_unequal_adjacent_groups_subsequence_ii", r'''
# LeetCode 2901 - Longest Unequal Adjacent Groups Subsequence II
# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

# @param {String[]} words
# @param {Integer[]} groups
# @return {String[]}
def get_words_in_longest_subsequence(words, groups)
  n = words.length
  dp = Array.new(n, 1)
  prev = Array.new(n, -1)

  hamming = lambda do |a, b|
    return 100 if a.length != b.length

    (0...a.length).count { |i| a[i] != b[i] }
  end

  best = 1
  best_i = 0
  (0...n).each do |i|
    (0...i).each do |j|
      if groups[i] != groups[j] && hamming.call(words[i], words[j]) == 1 && dp[j] + 1 >= dp[i]
        dp[i] = dp[j] + 1
        prev[i] = j
      end
    end
    if dp[i] >= best
      best = dp[i]
      best_i = i
    end
  end
  path = []
  i = best_i
  while i != -1
    path << words[i]
    i = prev[i]
  end
  path.reverse
end
''')

add("2902_count_of_sub_multisets_with_bounded_sum", r'''
# LeetCode 2902 - Count of Sub-Multisets With Bounded Sum
# https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/

# @param {Integer[]} nums
# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def count_sub_multisets(nums, l, r)
  mod = 1_000_000_007
  freq = {}
  total = 0
  nums.each do |v|
    freq[v] = freq.fetch(v, 0) + 1
    total += v
  end
  return 0 if total < l

  r = total if r > total
  dp = Array.new(r + 1, 0)
  dp[0] = 1
  zeros = freq.fetch(0, 0)
  freq.delete(0)
  freq.each do |v, c|
    ndp = Array.new(r + 1, 0)
    (0..r).each do |s|
      next if dp[s] == 0

      k = 0
      while k <= c && s + k * v <= r
        ndp[s + k * v] = (ndp[s + k * v] + dp[s]) % mod
        k += 1
      end
    end
    dp = ndp
  end
  ans = 0
  (l..r).each { |s| ans = (ans + dp[s]) % mod }
  (ans * (zeros + 1)) % mod
end
''')

add("2903_find_indices_with_index_and_value_difference_i", r'''
# LeetCode 2903 - Find Indices With Index and Value Difference I
# https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

# @param {Integer[]} nums
# @param {Integer} index_difference
# @param {Integer} value_difference
# @return {Integer[]}
def find_indices(nums, index_difference, value_difference)
  n = nums.length
  (0...n).each do |i|
    (i...n).each do |j|
      if (j - i).abs >= index_difference && (nums[i] - nums[j]).abs >= value_difference
        return [i, j]
      end
    end
  end
  [-1, -1]
end
''')

add("2904_shortest_and_lexicographically_smallest_beautiful_string", r'''
# LeetCode 2904 - Shortest and Lexicographically Smallest Beautiful String
# https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

# @param {String} s
# @param {Integer} k
# @return {String}
def shortest_beautiful_substring(s, k)
  ans = ""
  n = s.length
  (0...n).each do |i|
    ones = 0
    (i...n).each do |j|
      ones += 1 if s[j] == "1"
      if ones == k
        cand = s[i..j]
        if ans.empty? || cand.length < ans.length || (cand.length == ans.length && cand < ans)
          ans = cand
        end
        break
      end
      break if ones > k
    end
  end
  ans
end
''')

add("2905_find_indices_with_index_and_value_difference_ii", r'''
# LeetCode 2905 - Find Indices With Index and Value Difference II
# https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

# @param {Integer[]} nums
# @param {Integer} index_difference
# @param {Integer} value_difference
# @return {Integer[]}
def find_indices(nums, index_difference, value_difference)
  n = nums.length
  min_idx = 0
  max_idx = 0
  (index_difference...n).each do |j|
    i = j - index_difference
    min_idx = i if nums[i] < nums[min_idx]
    max_idx = i if nums[i] > nums[max_idx]
    return [min_idx, j] if nums[j] - nums[min_idx] >= value_difference
    return [max_idx, j] if nums[max_idx] - nums[j] >= value_difference
  end
  [-1, -1]
end
''')

add("2906_construct_product_matrix", r'''
# LeetCode 2906 - Construct Product Matrix
# https://leetcode.com/problems/construct-product-matrix/

# @param {Integer[][]} grid
# @return {Integer[][]}
def construct_product_matrix(grid)
  mod = 12345
  m = grid.length
  n = grid[0].length
  ans = Array.new(m) { Array.new(n, 0) }
  pref = 1
  (0...m).each do |i|
    (0...n).each do |j|
      ans[i][j] = pref
      pref = (pref * (grid[i][j] % mod)) % mod
    end
  end
  suf = 1
  (m - 1).downto(0) do |i|
    (n - 1).downto(0) do |j|
      ans[i][j] = (ans[i][j] * suf) % mod
      suf = (suf * (grid[i][j] % mod)) % mod
    end
  end
  ans
end
''')

add("2907_maximum_profitable_triplets_with_increasing_prices_i", r'''
# LeetCode 2907 - Maximum Profitable Triplets With Increasing Prices I
# https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-i/

# @param {Integer[]} prices
# @param {Integer[]} profits
# @return {Integer}
def max_profit(prices, profits)
  n = prices.length
  ans = -1
  (0...n).each do |j|
    best_l = -1
    best_r = -1
    (0...j).each do |i|
      best_l = profits[i] if prices[i] < prices[j] && profits[i] > best_l
    end
    (j + 1...n).each do |k|
      best_r = profits[k] if prices[k] > prices[j] && profits[k] > best_r
    end
    if best_l >= 0 && best_r >= 0
      cand = best_l + profits[j] + best_r
      ans = cand if cand > ans
    end
  end
  ans
end
''')

add("2908_minimum_sum_of_mountain_triplets_i", r'''
# LeetCode 2908 - Minimum Sum of Mountain Triplets I
# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/

# @param {Integer[]} nums
# @return {Integer}
def minimum_sum(nums)
  n = nums.length
  ans = 1 << 30
  (1...n - 1).each do |j|
    left = 1 << 30
    right = 1 << 30
    (0...j).each do |i|
      left = nums[i] if nums[i] < nums[j] && nums[i] < left
    end
    (j + 1...n).each do |k|
      right = nums[k] if nums[k] < nums[j] && nums[k] < right
    end
    if left < (1 << 30) && right < (1 << 30)
      cand = left + nums[j] + right
      ans = cand if cand < ans
    end
  end
  ans == (1 << 30) ? -1 : ans
end
''')

add("2909_minimum_sum_of_mountain_triplets_ii", r'''
# LeetCode 2909 - Minimum Sum of Mountain Triplets II
# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/

# @param {Integer[]} nums
# @return {Integer}
def minimum_sum(nums)
  n = nums.length
  left = Array.new(n, 0)
  right = Array.new(n, 0)
  mn = 1 << 30
  (0...n).each do |i|
    left[i] = mn
    mn = nums[i] if nums[i] < mn
  end
  mn = 1 << 30
  (n - 1).downto(0) do |i|
    right[i] = mn
    mn = nums[i] if nums[i] < mn
  end
  ans = 1 << 30
  (1...n - 1).each do |j|
    if left[j] < nums[j] && right[j] < nums[j]
      cand = left[j] + nums[j] + right[j]
      ans = cand if cand < ans
    end
  end
  ans == (1 << 30) ? -1 : ans
end
''')


def main() -> None:
    written = 0
    missing = []
    for name, body in S.items():
        path = ROOT / name / "solution.rb"
        if not path.parent.exists():
            missing.append(name)
            continue
        path.write_text(body, encoding="utf-8", newline="\n")
        written += 1
    print(f"wrote={written} missing={missing}")


if __name__ == "__main__":
    main()
