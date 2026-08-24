#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["2304_minimum_path_cost_in_a_grid"] = r'''# LeetCode 2304 - Minimum Path Cost in a Grid
# https://leetcode.com/problems/minimum-path-cost-in-a-grid/

# @param {Integer[][]} grid
# @param {Integer[][]} move_cost
# @return {Integer}
def min_path_cost(grid, move_cost)
  m = grid.length
  n = grid[0].length
  dp = grid[0].dup
  (0...m - 1).each do |r|
    nxt = Array.new(n, 2147483647 / 2)
    (0...n).each do |c|
      frm = grid[r][c]
      (0...n).each do |nc|
        nxt[nc] = [nxt[nc], dp[c] + move_cost[frm][nc] + grid[r + 1][nc]].min
      end
    end
    dp = nxt
  end
  ans = dp[0]
  (1...n).each { |i| ans = [ans, dp[i]].min }
  ans
end
'''

FILES["2305_fair_distribution_of_cookies"] = r'''# LeetCode 2305 - Fair Distribution of Cookies
# https://leetcode.com/problems/fair-distribution-of-cookies/

# @param {Integer[]} cookies
# @param {Integer} k
# @return {Integer}
def distribute_cookies(cookies, k)
  bags = Array.new(k, 0)
  ans = [Float::INFINITY]
  dfs = lambda do |i|
    if i == cookies.length
      mx = bags.max
      ans[0] = mx if mx < ans[0]
      return
    end
    seen = {}
    bags.each_index do |j|
      next if seen[bags[j]]
      seen[bags[j]] = true
      bags[j] += cookies[i]
      dfs.call(i + 1) if bags[j] < ans[0]
      bags[j] -= cookies[i]
      break if bags[j] == 0
    end
  end
  dfs.call(0)
  ans[0].to_i
end
'''

FILES["2306_naming_a_company"] = r'''# LeetCode 2306 - Naming a Company
# https://leetcode.com/problems/naming-a-company/

# @param {String[]} ideas
# @return {Integer}
def distinct_names(ideas)
  groups = Array.new(26) { {} }
  ideas.each do |idea|
    groups[idea[0].ord - 97][idea[1..]] = true
  end
  ans = 0
  (0...26).each do |i|
    ((i + 1)...26).each do |j|
      overlap = 0
      groups[i].each_key { |s| overlap += 1 if groups[j].key?(s) }
      ans += (groups[i].length - overlap) * (groups[j].length - overlap) * 2
    end
  end
  ans
end
'''

FILES["2307_check_for_contradictions_in_equations"] = r'''# LeetCode 2307 - Check for Contradictions in Equations
# https://leetcode.com/problems/check-for-contradictions-in-equations/

# @param {String[][]} equations
# @param {Float[]} values
# @return {Boolean}
def check_contradictions(equations, values)
  parent = {}
  weight = {}
  find = lambda do |x|
    unless parent.key?(x)
      parent[x] = x
      weight[x] = 1.0
      return x
    end
    if parent[x] != x
      old = parent[x]
      p = find.call(old)
      weight[x] = weight[x] * weight[old]
      parent[x] = p
    end
    parent[x]
  end
  equations.each_with_index do |(a, b), i|
    ra = find.call(a)
    rb = find.call(b)
    if ra == rb
      return true if (weight[a] / weight[b] - values[i]).abs > 1e-5
    else
      parent[ra] = rb
      weight[ra] = values[i] * weight[b] / weight[a]
    end
  end
  false
end
'''

FILES["2309_greatest_english_letter_in_upper_and_lower_case"] = r'''# LeetCode 2309 - Greatest English Letter in Upper and Lower Case
# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

# @param {String} s
# @return {String}
def greatest_letter(s)
  lower = Array.new(26, false)
  upper = Array.new(26, false)
  s.each_char do |c|
    if c >= "a" && c <= "z"
      lower[c.ord - 97] = true
    else
      upper[c.ord - 65] = true
    end
  end
  25.downto(0) do |i|
    return (65 + i).chr if lower[i] && upper[i]
  end
  ""
end
'''

FILES["2310_sum_of_numbers_with_units_digit_k"] = r'''# LeetCode 2310 - Sum of Numbers With Units Digit K
# https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/

# @param {Integer} num
# @param {Integer} k
# @return {Integer}
def minimum_numbers(num, k)
  return 0 if num == 0
  (1..10).each do |count|
    return count if count * k % 10 == num % 10 && count * k <= num
  end
  -1
end
'''

FILES["2311_longest_binary_subsequence_less_than_or_equal_to_k"] = r'''# LeetCode 2311 - Longest Binary Subsequence Less Than or Equal to K
# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def longest_subsequence(s, k)
  zeros = s.count("0")
  val = 0
  ones = 0
  pow2 = 1
  (s.length - 1).downto(0) do |i|
    if s[i] == "1"
      unless pow2 > k || val + pow2 > k
        val += pow2
        ones += 1
      end
    end
    pow2 *= 2 if pow2 <= k
  end
  zeros + ones
end
'''

FILES["2312_selling_pieces_of_wood"] = r'''# LeetCode 2312 - Selling Pieces of Wood
# https://leetcode.com/problems/selling-pieces-of-wood/

# @param {Integer} m
# @param {Integer} n
# @param {Integer[][]} prices
# @return {Integer}
def selling_wood(m, n, prices)
  price = Array.new(m + 1) { Array.new(n + 1, 0) }
  dp = Array.new(m + 1) { Array.new(n + 1, 0) }
  prices.each do |h, w, p|
    price[h][w] = p
  end
  (1..m).each do |h|
    (1..n).each do |w|
      best = price[h][w]
      (1...h).each { |i| best = [best, dp[i][w] + dp[h - i][w]].max }
      (1...w).each { |j| best = [best, dp[h][j] + dp[h][w - j]].max }
      dp[h][w] = best
    end
  end
  dp[m][n]
end
'''

FILES["2313_minimum_flips_in_binary_tree_to_get_result"] = r'''# LeetCode 2313 - Minimum Flips in Binary Tree to Get Result
# https://leetcode.com/problems/minimum-flips-in-binary-tree-to-get-result/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Boolean} result
# @return {Integer}
def minimum_flips(root, result)
  dfs = lambda do |node|
    if node.left.nil? && node.right.nil?
      return node.val == 0 ? [0, 1] : [1, 0]
    end
    if node.val == 5
      x = dfs.call(node.left)
      return [x[1], x[0]]
    end
    l = dfs.call(node.left)
    r = dfs.call(node.right)
    lf, lt, rf, rt = l[0], l[1], r[0], r[1]
    return [lf + rf, [lt + rt, lt + rf, lf + rt].min] if node.val == 2
    return [[lf + rf, lf + rt, lt + rf].min, lt + rt] if node.val == 3
    return [[lf + rf, lt + rt].min, [lf + rt, lt + rf].min] if node.val == 4
    [0, 0]
  end
  res = dfs.call(root)
  result ? res[1] : res[0]
end
'''

FILES["2315_count_asterisks"] = r'''# LeetCode 2315 - Count Asterisks
# https://leetcode.com/problems/count-asterisks/

# @param {String} s
# @return {Integer}
def count_asterisks(s)
  ans = 0
  inside = false
  s.each_char do |c|
    if c == "|"
      inside = !inside
    elsif c == "*" && !inside
      ans += 1
    end
  end
  ans
end
'''

FILES["2316_count_unreachable_pairs_of_nodes_in_an_undirected_graph"] = r'''# LeetCode 2316 - Count Unreachable Pairs of Nodes in an Undirected Graph
# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def count_pairs(n, edges)
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  vis = Array.new(n, false)
  dfs = lambda do |u|
    vis[u] = true
    size = 1
    g[u].each { |v| size += dfs.call(v) unless vis[v] }
    size
  end
  ans = 0
  seen = 0
  (0...n).each do |i|
    next if vis[i]
    sz = dfs.call(i)
    ans += sz * seen
    seen += sz
  end
  ans
end
'''

FILES["2317_maximum_xor_after_operations"] = r'''# LeetCode 2317 - Maximum XOR After Operations
# https://leetcode.com/problems/maximum-xor-after-operations/

# @param {Integer[]} nums
# @return {Integer}
def maximum_xor(nums)
  ans = 0
  nums.each { |x| ans |= x }
  ans
end
'''

FILES["2318_number_of_distinct_roll_sequences"] = r'''# LeetCode 2318 - Number of Distinct Roll Sequences
# https://leetcode.com/problems/number-of-distinct-roll-sequences/

# @param {Integer} n
# @return {Integer}
def distinct_sequences(n)
  mod = 1_000_000_007
  gcd = lambda do |a, b|
    a, b = b, a % b while b != 0
    a
  end
  dp = Array.new(n + 1) { Array.new(7) { Array.new(7, 0) } }
  (1..6).each { |a| dp[1][a][0] = 1 }
  (2..n).each do |i|
    (1..6).each do |prev|
      (0..6).each do |pprev|
        next if dp[i - 1][prev][pprev] == 0
        (1..6).each do |cur|
          next if cur == prev || cur == pprev || gcd.call(cur, prev) != 1
          dp[i][cur][prev] = (dp[i][cur][prev] + dp[i - 1][prev][pprev]) % mod
        end
      end
    end
  end
  ans = 0
  (1..6).each do |a|
    (0..6).each { |b| ans = (ans + dp[n][a][b]) % mod }
  end
  ans
end
'''

FILES["2319_check_if_matrix_is_x_matrix"] = r'''# LeetCode 2319 - Check if Matrix Is X-Matrix
# https://leetcode.com/problems/check-if-matrix-is-x-matrix/

# @param {Integer[][]} grid
# @return {Boolean}
def check_x_matrix(grid)
  n = grid.length
  (0...n).each do |i|
    (0...n).each do |j|
      diag = i == j || i + j == n - 1
      if diag
        return false if grid[i][j] == 0
      elsif grid[i][j] != 0
        return false
      end
    end
  end
  true
end
'''

FILES["2320_count_number_of_ways_to_place_houses"] = r'''# LeetCode 2320 - Count Number of Ways to Place Houses
# https://leetcode.com/problems/count-number-of-ways-to-place-houses/

# @param {Integer} n
# @return {Integer}
def count_house_placements(n)
  mod = 1_000_000_007
  a = 1
  b = 1
  n.times do
    na = (a + b) % mod
    b = a
    a = na
  end
  ways = (a + b) % mod
  ways * ways % mod
end
'''

FILES["2321_maximum_score_of_spliced_array"] = r'''# LeetCode 2321 - Maximum Score Of Spliced Array
# https://leetcode.com/problems/maximum-score-of-spliced-array/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def maximums_spliced_array(nums1, nums2)
  kadane = lambda do |a, b|
    best = 0
    cur = 0
    s = 0
    a.each_index do |i|
      s += a[i]
      cur += b[i] - a[i]
      cur = 0 if cur < 0
      best = cur if cur > best
    end
    s + best
  end
  [kadane.call(nums1, nums2), kadane.call(nums2, nums1)].max
end
'''

FILES["2322_minimum_score_after_removals_on_a_tree"] = r'''# LeetCode 2322 - Minimum Score After Removals on a Tree
# https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

# @param {Integer[]} nums
# @param {Integer[][]} edges
# @return {Integer}
def minimum_score(nums, edges)
  n = nums.length
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  xorv = Array.new(n, 0)
  in_t = Array.new(n, 0)
  out_t = Array.new(n, 0)
  time = [0]
  dfs = lambda do |u, p|
    in_t[u] = time[0]
    time[0] += 1
    xorv[u] = nums[u]
    g[u].each do |v|
      if v != p
        dfs.call(v, u)
        xorv[u] ^= xorv[v]
      end
    end
    out_t[u] = time[0]
  end
  is_ancestor = lambda do |a, b|
    in_t[a] <= in_t[b] && out_t[b] <= out_t[a]
  end
  dfs.call(0, -1)
  total = xorv[0]
  ans = Float::INFINITY
  (1...n).each do |i|
    ((i + 1)...n).each do |j|
      if is_ancestor.call(i, j)
        a = xorv[j]
        b = xorv[i] ^ xorv[j]
        c = total ^ xorv[i]
      elsif is_ancestor.call(j, i)
        a = xorv[i]
        b = xorv[j] ^ xorv[i]
        c = total ^ xorv[j]
      else
        a = xorv[i]
        b = xorv[j]
        c = total ^ xorv[i] ^ xorv[j]
      end
      cand = [a, b, c].max - [a, b, c].min
      ans = cand if cand < ans
    end
  end
  ans.to_i
end
'''

FILES["2323_find_minimum_time_to_finish_all_jobs_ii"] = r'''# LeetCode 2323 - Find Minimum Time to Finish All Jobs II
# https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/

# @param {Integer[]} jobs
# @param {Integer[]} workers
# @return {Integer}
def minimum_time(jobs, workers)
  jobs = jobs.sort
  workers = workers.sort
  ans = 0
  jobs.each_index do |i|
    cand = (jobs[i] + workers[i] - 1) / workers[i]
    ans = cand if cand > ans
  end
  ans
end
'''

FILES["2325_decode_the_message"] = r'''# LeetCode 2325 - Decode the Message
# https://leetcode.com/problems/decode-the-message/

# @param {String} key
# @param {String} message
# @return {String}
def decode_message(key, message)
  mp = Array.new(26, 0)
  nxt = 97
  key.each_char do |c|
    next if c == " " || mp[c.ord - 97] != 0
    mp[c.ord - 97] = nxt
    nxt += 1
  end
  out = message.chars
  out.each_index do |i|
    out[i] = mp[out[i].ord - 97].chr if out[i] != " "
  end
  out.join
end
'''

FILES["2326_spiral_matrix_iv"] = r'''# LeetCode 2326 - Spiral Matrix IV
# https://leetcode.com/problems/spiral-matrix-iv/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {Integer} m
# @param {Integer} n
# @param {ListNode} head
# @return {Integer[][]}
def spiral_matrix(m, n, head)
  ans = Array.new(m) { Array.new(n, -1) }
  dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  r = 0
  c = 0
  d = 0
  until head.nil?
    ans[r][c] = head.val
    head = head.next
    nr = r + dirs[d][0]
    nc = c + dirs[d][1]
    if nr < 0 || nr >= m || nc < 0 || nc >= n || ans[nr][nc] != -1
      d = (d + 1) % 4
      nr = r + dirs[d][0]
      nc = c + dirs[d][1]
    end
    r = nr
    c = nc
  end
  ans
end
'''

for folder, content in FILES.items():
    path = ROOT / folder / "solution.rb"
    path.write_text(content, encoding="utf-8", newline="\n")
    if content.startswith("\ufeff"):
        raise SystemExit(f"BOM in {folder}")
    print(f"wrote {folder}")
print(f"done {len(FILES)}")
