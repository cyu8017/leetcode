#!/usr/bin/env python3
from pathlib import Path

root = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")


def hdr(num, title, slug):
    return f"# LeetCode {num} - {title}\n# https://leetcode.com/problems/{slug}/\n\n"


files = {}

files["2006_count_number_of_pairs_with_absolute_difference_k"] = hdr("2006", "Count Number of Pairs With Absolute Difference K", "count-number-of-pairs-with-absolute-difference-k") + """# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_k_difference(nums, k)
  freq = Hash.new(0)
  ans = 0
  nums.each do |x|
    ans += freq[x - k]
    ans += freq[x + k]
    freq[x] += 1
  end
  ans
end
"""

files["2007_find_original_array_from_doubled_array"] = hdr("2007", "Find Original Array From Doubled Array", "find-original-array-from-doubled-array") + """# @param {Integer[]} changed
# @return {Integer[]}
def find_original_array(changed)
  return [] if changed.length.odd?

  changed.sort!
  freq = Hash.new(0)
  changed.each { |x| freq[x] += 1 }
  ans = []
  changed.each do |x|
    next if freq[x].zero?

    freq[x] -= 1
    return [] if freq[2 * x].zero?

    freq[2 * x] -= 1
    ans << x
  end
  ans
end
"""

files["2008_maximum_earnings_from_taxi"] = hdr("2008", "Maximum Earnings From Taxi", "maximum-earnings-from-taxi") + """# @param {Integer} n
# @param {Integer[][]} rides
# @return {Integer}
def max_taxi_earnings(n, rides)
  rides.sort_by! { |r| r[1] }
  m = rides.length
  ends = rides.map { |r| r[1] }
  dp = Array.new(m + 1, 0)
  rides.each_with_index do |(start, finish, tip), i|
    earn = finish - start + tip
    lo = 0
    hi = m
    while lo < hi
      mid = (lo + hi) >> 1
      if ends[mid] <= start
        lo = mid + 1
      else
        hi = mid
      end
    end
    dp[i + 1] = [dp[i], earn + dp[lo]].max
  end
  dp[m]
end
"""

files["2009_minimum_number_of_operations_to_make_array_continuous"] = hdr("2009", "Minimum Number of Operations to Make Array Continuous", "minimum-number-of-operations-to-make-array-continuous") + """# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  n = nums.length
  uniq = nums.uniq.sort
  ans = n
  j = 0
  uniq.each_index do |i|
    j += 1 while j < uniq.length && uniq[j] - uniq[i] + 1 <= n
    ans = [ans, n - (j - i)].min
  end
  ans
end
"""

files["2011_final_value_of_variable_after_performing_operations"] = hdr("2011", "Final Value of Variable After Performing Operations", "final-value-of-variable-after-performing-operations") + """# @param {String[]} operations
# @return {Integer}
def final_value_after_operations(operations)
  x = 0
  operations.each { |op| op[1] == "+" ? x += 1 : x -= 1 }
  x
end
"""

files["2012_sum_of_beauty_in_the_array"] = hdr("2012", "Sum of Beauty in the Array", "sum-of-beauty-in-the-array") + """# @param {Integer[]} nums
# @return {Integer}
def sum_of_beauties(nums)
  n = nums.length
  prefix_max = Array.new(n, 0)
  suffix_min = Array.new(n, 0)
  prefix_max[0] = nums[0]
  (1...n).each { |i| prefix_max[i] = [prefix_max[i - 1], nums[i]].max }
  suffix_min[n - 1] = nums[n - 1]
  (n - 2).downto(0) { |i| suffix_min[i] = [suffix_min[i + 1], nums[i]].min }
  ans = 0
  (1...n - 1).each do |i|
    if prefix_max[i - 1] < nums[i] && nums[i] < suffix_min[i + 1]
      ans += 2
    elsif nums[i - 1] < nums[i] && nums[i] < nums[i + 1]
      ans += 1
    end
  end
  ans
end
"""

files["2013_detect_squares"] = hdr("2013", "Detect Squares", "detect-squares") + """class DetectSquares
  def initialize
    @cnt = Hash.new(0)
  end

  def add(point)
    @cnt[key(point[0], point[1])] += 1
  end

  def count(point)
    x = point[0]
    y = point[1]
    ans = 0
    @cnt.each do |k, c|
      px, py = k.split(",").map(&:to_i)
      next if px == x || py == y
      next if (px - x).abs != (py - y).abs

      ans += c * @cnt[key(px, y)] * @cnt[key(x, py)]
    end
    ans
  end

  private

  def key(x, y)
    "#{x},#{y}"
  end
end
"""

files["2014_longest_subsequence_repeated_k_times"] = hdr("2014", "Longest Subsequence Repeated k Times", "longest-subsequence-repeated-k-times") + """# @param {String} s
# @param {Integer} k
# @return {String}
def longest_subsequence_repeated_k(s, k)
  freq = Array.new(26, 0)
  s.each_char { |c| freq[c.ord - 97] += 1 }
  chars = (25).downto(0).filter_map { |c| (97 + c).chr if freq[c] >= k }.join

  is_subseq = lambda do |t|
    need = 0
    times = 0
    s.each_char do |ch|
      next unless ch == t[need]

      need += 1
      if need == t.length
        times += 1
        return true if times == k

        need = 0
      end
    end
    false
  end

  best = ""
  q = [""]
  until q.empty?
    cur = q.shift
    chars.each_char do |ch|
      nxt = cur + ch
      next unless is_subseq.call(nxt)

      best = nxt if nxt.length > best.length || (nxt.length == best.length && nxt > best)
      q << nxt
    end
  end
  best
end
"""

files["2015_average_height_of_buildings_in_each_segment"] = hdr("2015", "Average Height of Buildings in Each Segment", "average-height-of-buildings-in-each-segment") + """# @param {Integer[][]} buildings
# @return {Integer[][]}
def average_height_of_buildings(buildings)
  events = []
  buildings.each do |left, right, h|
    events << [left, 1, h]
    events << [right, -1, h]
  end
  events.sort_by! { |e| [e[0], e[1]] }
  ans = []
  count = 0
  total = 0
  prev = events[0][0]
  events.each do |pos, typ, h|
    if pos != prev && count > 0
      avg = total / count
      if !ans.empty? && ans[-1][1] == prev && ans[-1][2] == avg
        ans[-1][1] = pos
      else
        ans << [prev, pos, avg]
      end
    end
    count += typ
    total += typ * h
    prev = pos
  end
  ans
end
"""

files["2016_maximum_difference_between_increasing_elements"] = hdr("2016", "Maximum Difference Between Increasing Elements", "maximum-difference-between-increasing-elements") + """# @param {Integer[]} nums
# @return {Integer}
def maximum_difference(nums)
  ans = -1
  mn = nums[0]
  (1...nums.length).each do |i|
    if nums[i] > mn
      ans = [ans, nums[i] - mn].max
    else
      mn = nums[i]
    end
  end
  ans
end
"""

files["2017_grid_game"] = hdr("2017", "Grid Game", "grid-game") + """# @param {Integer[][]} grid
# @return {Integer}
def grid_game(grid)
  n = grid[0].length
  top = grid[0].sum
  bottom = 0
  ans = 10**18
  n.times do |i|
    top -= grid[0][i]
    ans = [ans, [top, bottom].max].min
    bottom += grid[1][i]
  end
  ans
end
"""

files["2018_check_if_word_can_be_placed_in_crossword"] = hdr("2018", "Check if Word Can Be Placed In Crossword", "check-if-word-can-be-placed-in-crossword") + """# @param {Character[][]} board
# @param {String} word
# @return {Boolean}
def place_word_in_crossword(board, word)
  m = board.length
  n = board[0].length
  len = word.length

  match = lambda do |cells|
    return false if cells.length != len

    ok1 = ok2 = true
    len.times do |i|
      ok1 = false if cells[i] != " " && cells[i] != word[i]
      ok2 = false if cells[i] != " " && cells[i] != word[len - 1 - i]
    end
    ok1 || ok2
  end

  m.times do |r|
    c = 0
    while c < n
      c += 1 while c < n && board[r][c] == "#"
      start = c
      c += 1 while c < n && board[r][c] != "#"
      if c - start == len
        sb = (start...c).map { |i| board[r][i] }.join
        return true if match.call(sb)
      end
    end
  end
  n.times do |c|
    r = 0
    while r < m
      r += 1 while r < m && board[r][c] == "#"
      start = r
      r += 1 while r < m && board[r][c] != "#"
      if r - start == len
        sb = (0...len).map { |i| board[start + i][c] }.join
        return true if match.call(sb)
      end
    end
  end
  false
end
"""

files["2019_the_score_of_students_solving_math_expression"] = hdr("2019", "The Score of Students Solving Math Expression", "the-score-of-students-solving-math-expression") + """# @param {String} s
# @param {Integer[]} answers
# @return {Integer}
def score_of_students(s, answers)
  eval_correct = lambda do |expr|
    nums = []
    ops = []
    expr.each_char do |c|
      if c >= "0" && c <= "9"
        nums << c.ord - 48
      else
        ops << c
      end
    end
    new_nums = [nums[0]]
    new_ops = []
    ops.each_with_index do |op, j|
      if op == "*"
        new_nums[-1] *= nums[j + 1]
      else
        new_ops << op
        new_nums << nums[j + 1]
      end
    end
    res = new_nums[0]
    new_ops.each_index { |j| res += new_nums[j + 1] }
    res
  end

  n = s.length
  correct = eval_correct.call(s)
  dp = Array.new(n) { Array.new(n) }

  dfs = lambda do |l, r|
    return dp[l][r] unless dp[l][r].nil?

    res = {}
    if l == r
      res[s[l].ord - 48] = true
      dp[l][r] = res
      return res
    end
    i = l + 1
    while i < r
      dfs.call(l, i - 1).each_key do |a|
        dfs.call(i + 1, r).each_key do |b|
          v = s[i] == "+" ? a + b : a * b
          res[v] = true if v <= 1000
        end
      end
      i += 2
    end
    dp[l][r] = res
    res
  end

  possible = dfs.call(0, n - 1)
  ans = 0
  answers.each do |a|
    if a == correct
      ans += 5
    elsif possible[a]
      ans += 2
    end
  end
  ans
end
"""

files["2021_brightest_position_on_street"] = hdr("2021", "Brightest Position on Street", "brightest-position-on-street") + """# @param {Integer[][]} lights
# @return {Integer}
def brightest_position(lights)
  events = []
  lights.each do |pos, r|
    events << [pos - r, 1]
    events << [pos + r + 1, -1]
  end
  events.sort_by! { |e| [e[0], -e[1]] }
  best = 0
  cur = 0
  ans = 0
  events.each do |pos, d|
    cur += d
    if cur > best
      best = cur
      ans = pos
    end
  end
  ans
end
"""

files["2022_convert_1d_array_into_2d_array"] = hdr("2022", "Convert 1D Array Into 2D Array", "convert-1d-array-into-2d-array") + """# @param {Integer[]} original
# @param {Integer} m
# @param {Integer} n
# @return {Integer[][]}
def construct2_d_array(original, m, n)
  return [] if original.length != m * n

  ans = Array.new(m) { Array.new(n, 0) }
  m.times do |i|
    n.times { |j| ans[i][j] = original[i * n + j] }
  end
  ans
end
"""

files["2023_number_of_pairs_of_strings_with_concatenation_equal_to_target"] = hdr("2023", "Number of Pairs of Strings With Concatenation Equal to Target", "number-of-pairs-of-strings-with-concatenation-equal-to-target") + """# @param {String[]} nums
# @param {String} target
# @return {Integer}
def num_of_pairs(nums, target)
  ans = 0
  nums.each_index do |i|
    nums.each_index do |j|
      ans += 1 if i != j && nums[i] + nums[j] == target
    end
  end
  ans
end
"""

files["2024_maximize_the_confusion_of_an_exam"] = hdr("2024", "Maximize the Confusion of an Exam", "maximize-the-confusion-of-an-exam") + """# @param {String} answer_key
# @param {Integer} k
# @return {Integer}
def max_consecutive_answers(answer_key, k)
  max_with = lambda do |ch|
    left = bad = best = 0
    answer_key.each_char.with_index do |c, right|
      bad += 1 if c != ch
      while bad > k
        bad -= 1 if answer_key[left] != ch
        left += 1
      end
      best = [best, right - left + 1].max
    end
    best
  end
  [max_with.call("T"), max_with.call("F")].max
end
"""

files["2025_maximum_number_of_ways_to_partition_an_array"] = hdr("2025", "Maximum Number of Ways to Partition an Array", "maximum-number-of-ways-to-partition-an-array") + """# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def ways_to_partition(nums, k)
  n = nums.length
  pref = Array.new(n, 0)
  pref[0] = nums[0]
  (1...n).each { |i| pref[i] = pref[i - 1] + nums[i] }
  total = pref[n - 1]
  right = Hash.new(0)
  left = Hash.new(0)
  (0...n - 1).each { |i| right[pref[i]] += 1 }
  ans = 0
  ans = right[total / 2] if total.even?
  n.times do |i|
    diff = k - nums[i]
    new_total = total + diff
    cur = 0
    if new_total.even?
      half = new_total / 2
      cur = left[half] + right[half - diff]
    end
    ans = [ans, cur].max
    if i < n - 1
      left[pref[i]] += 1
      right[pref[i]] -= 1
    end
  end
  ans
end
"""

files["2027_minimum_moves_to_convert_string"] = hdr("2027", "Minimum Moves to Convert String", "minimum-moves-to-convert-string") + """# @param {String} s
# @return {Integer}
def minimum_moves(s)
  ans = 0
  i = 0
  while i < s.length
    if s[i] == "X"
      ans += 1
      i += 3
    else
      i += 1
    end
  end
  ans
end
"""

files["2028_find_missing_observations"] = hdr("2028", "Find Missing Observations", "find-missing-observations") + """# @param {Integer[]} rolls
# @param {Integer} mean
# @param {Integer} n
# @return {Integer[]}
def missing_rolls(rolls, mean, n)
  remain = mean * (rolls.length + n) - rolls.sum
  return [] if remain < n || remain > 6 * n

  base_val, extra = remain.divmod(n)
  Array.new(n) { |i| base_val + (i < extra ? 1 : 0) }
end
"""

files["2029_stone_game_ix"] = hdr("2029", "Stone Game IX", "stone-game-ix") + """# @param {Integer[]} stones
# @return {Boolean}
def stone_game_ix(stones)
  cnt = [0, 0, 0]
  stones.each { |s| cnt[s % 3] += 1 }
  if cnt[0].even?
    cnt[1] > 0 && cnt[2] > 0
  else
    (cnt[1] - cnt[2]).abs > 2
  end
end
"""

files["2030_smallest_k_length_subsequence_with_occurrences_of_a_letter"] = hdr("2030", "Smallest K-Length Subsequence With Occurrences of a Letter", "smallest-k-length-subsequence-with-occurrences-of-a-letter") + """# @param {String} s
# @param {Integer} k
# @param {Character} letter
# @param {Integer} repetition
# @return {String}
def smallest_subsequence(s, k, letter, repetition)
  n = s.length
  remain_letter = s.chars.count(letter)
  stack = []
  in_stack_letter = 0
  s.each_char.with_index do |ch, i|
    while !stack.empty? && ch < stack[-1] && stack.length + n - i > k
      top = stack[-1]
      if top == letter
        break if in_stack_letter + remain_letter - 1 < repetition

        in_stack_letter -= 1
      end
      stack.pop
    end
    if stack.length < k
      if ch == letter
        stack << ch
        in_stack_letter += 1
      elsif k - stack.length > repetition - in_stack_letter
        stack << ch
      end
    end
    remain_letter -= 1 if ch == letter
  end
  stack.join
end
"""

files["2031_count_subarrays_with_more_ones_than_zeros"] = hdr("2031", "Count Subarrays With More Ones Than Zeros", "count-subarrays-with-more-ones-than-zeros") + """class Fenwick
  def initialize(n)
    @bit = Array.new(n + 2, 0)
  end

  def add(i, v)
    while i < @bit.length
      @bit[i] += v
      i += i & -i
    end
  end

  def sum(i)
    s = 0
    while i > 0
      s += @bit[i]
      i -= i & -i
    end
    s
  end
end

# @param {Integer[]} nums
# @return {Integer}
def subarrays_with_more_zeros_than_ones(nums)
  mod = 10**9 + 7
  n = nums.length
  offset = n + 1
  fw = Fenwick.new(2 * n + 5)
  pref = 0
  ans = 0
  fw.add(offset, 1)
  nums.each do |x|
    pref += x == 1 ? 1 : -1
    idx = pref + offset
    ans = (ans + fw.sum(idx - 1)) % mod
    fw.add(idx, 1)
  end
  ans
end
"""

files["2032_two_out_of_three"] = hdr("2032", "Two Out of Three", "two-out-of-three") + """# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer[]} nums3
# @return {Integer[]}
def two_out_of_three(nums1, nums2, nums3)
  s0 = nums1.to_h { |v| [v, true] }
  s1 = nums2.to_h { |v| [v, true] }
  s2 = nums3.to_h { |v| [v, true] }
  ans = []
  (1..100).each do |v|
    c = (s0[v] ? 1 : 0) + (s1[v] ? 1 : 0) + (s2[v] ? 1 : 0)
    ans << v if c >= 2
  end
  ans
end
"""

files["2033_minimum_operations_to_make_a_uni_value_grid"] = hdr("2033", "Minimum Operations to Make a Uni-Value Grid", "minimum-operations-to-make-a-uni-value-grid") + """# @param {Integer[][]} grid
# @param {Integer} x
# @return {Integer}
def min_operations(grid, x)
  vals = []
  bas = grid[0][0] % x
  grid.each do |row|
    row.each do |v|
      return -1 if v % x != bas

      vals << v
    end
  end
  vals.sort!
  median = vals[vals.length / 2]
  vals.sum { |v| (v - median).abs / x }
end
"""

written = 0
for folder, content in files.items():
    (root / folder / "solution.rb").write_bytes(content.encode("utf-8"))
    written += 1
print(f"wrote {written}")
