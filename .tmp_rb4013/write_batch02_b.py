#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

TREE = """class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end
"""

LISTN = """class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next_node = nil)
    @val = val
    @next = next_node
  end
end
"""


def header(num, title, slug):
    return (
        f"# LeetCode {num} - {title}\n"
        f"# https://leetcode.com/problems/{slug}/\n\n"
    )


FILES = {}

FILES["0830_positions_of_large_groups"] = header("0830", "Positions of Large Groups", "positions-of-large-groups") + """# @param {String} s
# @return {Integer[][]}
def large_group_positions(s)
  ans = []
  i = 0
  n = s.length
  while i < n
    j = i
    j += 1 while j < n && s[j] == s[i]
    ans << [i, j - 1] if j - i >= 3
    i = j
  end
  ans
end
"""

FILES["0831_masking_personal_information"] = header("0831", "Masking Personal Information", "masking-personal-information") + """# @param {String} s
# @return {String}
def mask_pii(s)
  if s.include?("@")
    name, domain = s.downcase.split("@")
    return "#{name[0]}*****#{name[-1]}@#{domain}"
  end
  digits = s.chars.select { |ch| ch.match?(/\\d/) }
  local = digits[-4..].join
  country = digits.length - 10
  return "***-***-#{local}" if country == 0

  "+" + ("*" * country) + "-***-***-#{local}"
end
"""

FILES["0832_flipping_an_image"] = header("0832", "Flipping an Image", "flipping-an-image") + """# @param {Integer[][]} image
# @return {Integer[][]}
def flip_and_invert_image(image)
  image.map { |row| row.reverse.map { |x| 1 - x } }
end
"""

FILES["0833_find_and_replace_in_string"] = header("0833", "Find And Replace in String", "find-and-replace-in-string") + """# @param {String} s
# @param {Integer[]} indices
# @param {String[]} sources
# @param {String[]} targets
# @return {String}
def find_replace_string(s, indices, sources, targets)
  replace = {}
  indices.zip(sources, targets).each do |i, src, tgt|
    replace[i] = [src.length, tgt] if s[i, src.length] == src
  end
  out = []
  i = 0
  while i < s.length
    if replace.key?(i)
      length, tgt = replace[i]
      out << tgt
      i += length
    else
      out << s[i]
      i += 1
    end
  end
  out.join
end
"""

FILES["0834_sum_of_distances_in_tree"] = header("0834", "Sum of Distances in Tree", "sum-of-distances-in-tree") + """# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer[]}
def sum_of_distances_in_tree(n, edges)
  graph = Hash.new { |h, k| h[k] = [] }
  edges.each do |a, b|
    graph[a] << b
    graph[b] << a
  end

  count = Array.new(n, 1)
  ans = Array.new(n, 0)

  post = lambda do |node, parent|
    graph[node].each do |child|
      next if child == parent

      post.call(child, node)
      count[node] += count[child]
      ans[node] += ans[child] + count[child]
    end
  end

  reroot = lambda do |node, parent|
    graph[node].each do |child|
      next if child == parent

      ans[child] = ans[node] - count[child] + (n - count[child])
      reroot.call(child, node)
    end
  end

  post.call(0, -1)
  reroot.call(0, -1)
  ans
end
"""

FILES["0835_image_overlap"] = header("0835", "Image Overlap", "image-overlap") + """# @param {Integer[][]} img1
# @param {Integer[][]} img2
# @return {Integer}
def largest_overlap(img1, img2)
  n = img1.length
  ones1 = []
  ones2 = []
  n.times do |i|
    n.times do |j|
      ones1 << [i, j] if img1[i][j] != 0
      ones2 << [i, j] if img2[i][j] != 0
    end
  end
  return 0 if ones1.empty? || ones2.empty?

  shifts = Hash.new(0)
  ones1.each do |x1, y1|
    ones2.each { |x2, y2| shifts[[x1 - x2, y1 - y2]] += 1 }
  end
  shifts.values.max
end
"""

FILES["0836_rectangle_overlap"] = header("0836", "Rectangle Overlap", "rectangle-overlap") + """# @param {Integer[]} rec1
# @param {Integer[]} rec2
# @return {Boolean}
def is_rectangle_overlap(rec1, rec2)
  !(rec1[2] <= rec2[0] || rec1[0] >= rec2[2] || rec1[3] <= rec2[1] || rec1[1] >= rec2[3])
end
"""

FILES["0837_new_21_game"] = header("0837", "New 21 Game", "new-21-game") + """# @param {Integer} n
# @param {Integer} k
# @param {Integer} max_pts
# @return {Float}
def new21_game(n, k, max_pts)
  return 1.0 if k == 0 || n >= k - 1 + max_pts

  dp = Array.new(n + 1, 0.0)
  dp[0] = 1.0
  window = 1.0
  ans = 0.0
  (1..n).each do |i|
    dp[i] = window / max_pts
    if i < k
      window += dp[i]
    else
      ans += dp[i]
    end
    window -= dp[i - max_pts] if i - max_pts >= 0 && i - max_pts < k
  end
  ans
end
"""

FILES["0838_push_dominoes"] = header("0838", "Push Dominoes", "push-dominoes") + """# @param {String} dominoes
# @return {String}
def push_dominoes(dominoes)
  n = dominoes.length
  force = Array.new(n, 0)
  f = 0
  n.times do |i|
    if dominoes[i] == "R"
      f = n
    elsif dominoes[i] == "L"
      f = 0
    else
      f = [f - 1, 0].max
    end
    force[i] += f
  end
  f = 0
  (n - 1).downto(0) do |i|
    if dominoes[i] == "L"
      f = n
    elsif dominoes[i] == "R"
      f = 0
    else
      f = [f - 1, 0].max
    end
    force[i] -= f
  end
  force.map { |x| x > 0 ? "R" : x < 0 ? "L" : "." }.join
end
"""

FILES["0839_similar_string_groups"] = header("0839", "Similar String Groups", "similar-string-groups") + """# @param {String[]} strs
# @return {Integer}
def num_similar_groups(strs)
  n = strs.length
  parent = (0...n).to_a

  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end

  similar = lambda do |a, b|
    diff = []
    a.length.times { |i| diff << i if a[i] != b[i] }
    diff.empty? || (diff.length == 2 && a[diff[0]] == b[diff[1]] && a[diff[1]] == b[diff[0]])
  end

  groups = n
  n.times do |i|
    ((i + 1)...n).each do |j|
      next unless similar.call(strs[i], strs[j])

      pi = find.call(i)
      pj = find.call(j)
      if pi != pj
        parent[pi] = pj
        groups -= 1
      end
    end
  end
  groups
end
"""

FILES["0840_magic_squares_in_grid"] = header("0840", "Magic Squares In Grid", "magic-squares-in-grid") + """# @param {Integer[][]} grid
# @return {Integer}
def num_magic_squares_inside(grid)
  rows = grid.length
  cols = grid[0].length
  return 0 if rows < 3 || cols < 3

  magic = lambda do |r, c|
    vals = (0...3).flat_map { |i| (0...3).map { |j| grid[r + i][c + j] } }
    return false if vals.sort != (1..9).to_a

    a = grid
    a[r][c] + a[r][c + 1] + a[r][c + 2] == 15 &&
      a[r + 1][c] + a[r + 1][c + 1] + a[r + 1][c + 2] == 15 &&
      a[r + 2][c] + a[r + 2][c + 1] + a[r + 2][c + 2] == 15 &&
      a[r][c] + a[r + 1][c] + a[r + 2][c] == 15 &&
      a[r][c + 1] + a[r + 1][c + 1] + a[r + 2][c + 1] == 15 &&
      a[r][c + 2] + a[r + 1][c + 2] + a[r + 2][c + 2] == 15 &&
      a[r][c] + a[r + 1][c + 1] + a[r + 2][c + 2] == 15 &&
      a[r][c + 2] + a[r + 1][c + 1] + a[r + 2][c] == 15
  end

  (0...rows - 2).sum { |i| (0...cols - 2).count { |j| magic.call(i, j) } }
end
"""

FILES["0841_keys_and_rooms"] = header("0841", "Keys and Rooms", "keys-and-rooms") + """# @param {Integer[][]} rooms
# @return {Boolean}
def can_visit_all_rooms(rooms)
  seen = { 0 => true }
  stack = [0]
  until stack.empty?
    room = stack.pop
    rooms[room].each do |key|
      next if seen[key]

      seen[key] = true
      stack << key
    end
  end
  seen.length == rooms.length
end
"""

FILES["0842_split_array_into_fibonacci_sequence"] = header("0842", "Split Array into Fibonacci Sequence", "split-array-into-fibonacci-sequence") + """# @param {String} num
# @return {Integer[]}
def split_into_fibonacci(num)
  n = num.length
  path = []

  dfs = lambda do |start|
    return path.length >= 3 if start == n

    (start...n).each do |finish|
      break if num[start] == "0" && finish > start

      val = num[start..finish].to_i
      break if val > 2**31 - 1

      if path.length >= 2
        total = path[-1] + path[-2]
        next if val < total
        break if val > total
      end
      path << val
      return true if dfs.call(finish + 1)

      path.pop
    end
    false
  end

  dfs.call(0)
  path
end
"""

FILES["0843_guess_the_word"] = header("0843", "Guess the Word", "guess-the-word") + """# @param {String[]} words
# @param {Object} master
# @return {Void}
def find_secret_word(words, master)
  match = ->(a, b) { a.chars.zip(b.chars).count { |x, y| x == y } }

  candidates = words.dup
  until candidates.empty?
    best = candidates.min_by do |w|
      (0..6).map { |m| candidates.count { |c| match.call(w, c) == m } }.max
    end
    score = master.guess(best)
    return if score == 6

    candidates = candidates.select { |c| match.call(c, best) == score }
  end
end
"""

FILES["0844_backspace_string_compare"] = header("0844", "Backspace String Compare", "backspace-string-compare") + """# @param {String} s
# @param {String} t
# @return {Boolean}
def backspace_compare(s, t)
  build = lambda do |text|
    stack = []
    text.each_char do |ch|
      if ch == "#"
        stack.pop unless stack.empty?
      else
        stack << ch
      end
    end
    stack
  end

  build.call(s) == build.call(t)
end
"""

FILES["0845_longest_mountain_in_array"] = header("0845", "Longest Mountain in Array", "longest-mountain-in-array") + """# @param {Integer[]} arr
# @return {Integer}
def longest_mountain(arr)
  n = arr.length
  ans = 0
  i = 0
  while i < n
    j = i
    if j + 1 < n && arr[j] < arr[j + 1]
      j += 1 while j + 1 < n && arr[j] < arr[j + 1]
      if j + 1 < n && arr[j] > arr[j + 1]
        j += 1 while j + 1 < n && arr[j] > arr[j + 1]
        ans = [ans, j - i + 1].max
        i = j
        next
      end
    end
    i += 1
  end
  ans
end
"""

FILES["0846_hand_of_straights"] = header("0846", "Hand of Straights", "hand-of-straights") + """# @param {Integer[]} hand
# @param {Integer} group_size
# @return {Boolean}
def is_n_straight_hand(hand, group_size)
  return false if hand.length % group_size != 0

  count = Hash.new(0)
  hand.each { |x| count[x] += 1 }
  count.keys.sort.each do |start|
    while count[start].positive?
      (start...start + group_size).each do |x|
        return false if count[x].zero?

        count[x] -= 1
      end
    end
  end
  true
end
"""

FILES["0847_shortest_path_visiting_all_nodes"] = header("0847", "Shortest Path Visiting All Nodes", "shortest-path-visiting-all-nodes") + """# @param {Integer[][]} graph
# @return {Integer}
def shortest_path_length(graph)
  n = graph.length
  target = (1 << n) - 1
  queue = (0...n).map { |i| [i, 1 << i, 0] }
  seen = {}
  n.times { |i| seen[[i, 1 << i]] = true }
  until queue.empty?
    node, mask, dist = queue.shift
    return dist if mask == target

    graph[node].each do |nxt|
      nmask = mask | (1 << nxt)
      state = [nxt, nmask]
      next if seen[state]

      seen[state] = true
      queue << [nxt, nmask, dist + 1]
    end
  end
  -1
end
"""

FILES["0848_shifting_letters"] = header("0848", "Shifting Letters", "shifting-letters") + """# @param {String} s
# @param {Integer[]} shifts
# @return {String}
def shifting_letters(s, shifts)
  total = 0
  chars = s.chars
  (s.length - 1).downto(0) do |i|
    total = (total + shifts[i]) % 26
    chars[i] = ((chars[i].ord - 97 + total) % 26 + 97).chr
  end
  chars.join
end
"""

FILES["0849_maximize_distance_to_closest_person"] = header("0849", "Maximize Distance to Closest Person", "maximize-distance-to-closest-person") + """# @param {Integer[]} seats
# @return {Integer}
def max_dist_to_closest(seats)
  n = seats.length
  prev = -1
  ans = 0
  seats.each_with_index do |occupied, i|
    next if occupied == 0

    ans = prev == -1 ? i : [ans, (i - prev) / 2].max
    prev = i
  end
  [ans, n - 1 - prev].max
end
"""

FILES["0850_rectangle_area_ii"] = header("0850", "Rectangle Area II", "rectangle-area-ii") + """# @param {Integer[][]} rectangles
# @return {Integer}
def rectangle_area(rectangles)
  mod = 10**9 + 7
  events = []
  rectangles.each do |x1, y1, x2, y2|
    events << [x1, 1, y1, y2]
    events << [x2, -1, y1, y2]
  end
  events.sort!

  covered_length = lambda do |active|
    return 0 if active.empty?

    active = active.sort
    total = 0
    cur_start, cur_end = active[0]
    active[1..].each do |start, finish|
      if start > cur_end
        total += cur_end - cur_start
        cur_start = start
        cur_end = finish
      else
        cur_end = [cur_end, finish].max
      end
    end
    total + cur_end - cur_start
  end

  active = []
  area = 0
  prev_x = events[0][0]
  events.each do |x, typ, y1, y2|
    area += covered_length.call(active) * (x - prev_x)
    if typ == 1
      active << [y1, y2]
    else
      idx = active.index([y1, y2])
      active.delete_at(idx)
    end
    prev_x = x
  end
  area % mod
end
"""

FILES["0851_loud_and_rich"] = header("0851", "Loud and Rich", "loud-and-rich") + """# @param {Integer[][]} richer
# @param {Integer[]} quiet
# @return {Integer[]}
def loud_and_rich(richer, quiet)
  n = quiet.length
  graph = Hash.new { |h, k| h[k] = [] }
  richer.each { |a, b| graph[b] << a }
  ans = Array.new(n, -1)

  dfs = lambda do |person|
    return ans[person] if ans[person] != -1

    best = person
    graph[person].each do |richer_person|
      cand = dfs.call(richer_person)
      best = cand if quiet[cand] < quiet[best]
    end
    ans[person] = best
  end

  n.times { |i| dfs.call(i) }
  ans
end
"""

FILES["0852_peak_index_in_a_mountain_array"] = header("0852", "Peak Index in a Mountain Array", "peak-index-in-a-mountain-array") + """# @param {Integer[]} arr
# @return {Integer}
def peak_index_in_mountain_array(arr)
  lo = 0
  hi = arr.length - 1
  while lo < hi
    mid = (lo + hi) / 2
    if arr[mid] < arr[mid + 1]
      lo = mid + 1
    else
      hi = mid
    end
  end
  lo
end
"""

FILES["0853_car_fleet"] = header("0853", "Car Fleet", "car-fleet") + """# @param {Integer} target
# @param {Integer[]} position
# @param {Integer[]} speed
# @return {Integer}
def car_fleet(target, position, speed)
  cars = position.zip(speed).sort.reverse
  fleets = 0
  max_time = 0.0
  cars.each do |pos, spd|
    time = (target - pos).to_f / spd
    if time > max_time
      fleets += 1
      max_time = time
    end
  end
  fleets
end
"""

FILES["0854_k_similar_strings"] = header("0854", "K-Similar Strings", "k-similar-strings") + """# @param {String} s1
# @param {String} s2
# @return {Integer}
def k_similarity(s1, s2)
  return 0 if s1 == s2

  target = s2
  queue = [[s1, 0]]
  seen = { s1 => true }

  neighbors = lambda do |s|
    arr = s.chars
    i = 0
    i += 1 while arr[i] == target[i]
    res = []
    ((i + 1)...arr.length).each do |j|
      next unless arr[j] == target[i] && arr[j] != target[j]

      arr[i], arr[j] = arr[j], arr[i]
      res << arr.join
      arr[i], arr[j] = arr[j], arr[i]
    end
    res
  end

  until queue.empty?
    cur, dist = queue.shift
    neighbors.call(cur).each do |nxt|
      return dist + 1 if nxt == target
      next if seen[nxt]

      seen[nxt] = true
      queue << [nxt, dist + 1]
    end
  end
  -1
end
"""

FILES["0855_exam_room"] = header("0855", "Exam Room", "exam-room") + """class ExamRoom
  def initialize(n)
    @n = n
    @seats = []
  end

  def seat
    if @seats.empty?
      @seats << 0
      return 0
    end

    best_seat = 0
    best_dist = @seats[0]
    (1...@seats.length).each do |i|
      dist = (@seats[i] - @seats[i - 1]) / 2
      if dist > best_dist
        best_dist = dist
        best_seat = @seats[i - 1] + dist
      end
    end
    best_seat = @n - 1 if @n - 1 - @seats[-1] > best_dist
    idx = @seats.bsearch_index { |x| x >= best_seat } || @seats.length
    @seats.insert(idx, best_seat)
    best_seat
  end

  def leave(p)
    @seats.delete(p)
  end
end
"""

FILES["0856_score_of_parentheses"] = header("0856", "Score of Parentheses", "score-of-parentheses") + """# @param {String} s
# @return {Integer}
def score_of_parentheses(s)
  stack = [0]
  s.each_char do |ch|
    if ch == "("
      stack << 0
    else
      val = stack.pop
      stack[-1] += [2 * val, 1].max
    end
  end
  stack[0]
end
"""

FILES["0857_minimum_cost_to_hire_k_workers"] = header("0857", "Minimum Cost to Hire K Workers", "minimum-cost-to-hire-k-workers") + """class MaxHeap
  def initialize
    @a = []
  end

  def size
    @a.size
  end

  def push(item)
    @a << item
    i = @a.size - 1
    while i.positive?
      p = (i - 1) / 2
      break if @a[p] >= @a[i]

      @a[p], @a[i] = @a[i], @a[p]
      i = p
    end
  end

  def pop
    top = @a[0]
    last = @a.pop
    return top if @a.empty?

    @a[0] = last
    i = 0
    loop do
      l = i * 2 + 1
      r = l + 1
      break if l >= @a.size

      largest = r < @a.size && @a[r] > @a[l] ? r : l
      break if @a[i] >= @a[largest]

      @a[i], @a[largest] = @a[largest], @a[i]
      i = largest
    end
    top
  end
end

# @param {Integer[]} quality
# @param {Integer[]} wage
# @param {Integer} k
# @return {Float}
def mincost_to_hire_workers(quality, wage, k)
  workers = quality.zip(wage).map { |q, w| [w.to_f / q, q] }.sort
  heap = MaxHeap.new
  total_q = 0
  ans = Float::INFINITY
  workers.each do |ratio, q|
    heap.push(q)
    total_q += q
    total_q -= heap.pop if heap.size > k
    ans = [ans, total_q * ratio].min if heap.size == k
  end
  ans
end
"""

FILES["0858_mirror_reflection"] = header("0858", "Mirror Reflection", "mirror-reflection") + """# @param {Integer} p
# @param {Integer} q
# @return {Integer}
def mirror_reflection(p, q)
  g = p.gcd(q)
  p /= g
  q /= g
  return 2 if p.even?
  return 0 if q.even?

  1
end
"""

FILES["0859_buddy_strings"] = header("0859", "Buddy Strings", "buddy-strings") + """# @param {String} s
# @param {String} goal
# @return {Boolean}
def buddy_strings(s, goal)
  return false if s.length != goal.length
  return s.chars.uniq.length < s.length if s == goal

  diffs = s.chars.zip(goal.chars).select { |a, b| a != b }
  diffs.length == 2 && diffs[0] == diffs[1].reverse
end
"""

FILES["0860_lemonade_change"] = header("0860", "Lemonade Change", "lemonade-change") + """# @param {Integer[]} bills
# @return {Boolean}
def lemonade_change(bills)
  fives = 0
  tens = 0
  bills.each do |bill|
    if bill == 5
      fives += 1
    elsif bill == 10
      return false if fives.zero?

      fives -= 1
      tens += 1
    elsif tens.positive? && fives.positive?
      tens -= 1
      fives -= 1
    elsif fives >= 3
      fives -= 3
    else
      return false
    end
  end
  true
end
"""

FILES["0861_score_after_flipping_matrix"] = header("0861", "Score After Flipping Matrix", "score-after-flipping-matrix") + """# @param {Integer[][]} grid
# @return {Integer}
def matrix_score(grid)
  m = grid.length
  n = grid[0].length
  grid.each do |row|
    next unless row[0] == 0

    n.times { |j| row[j] ^= 1 }
  end
  ans = m * (1 << (n - 1))
  (1...n).each do |j|
    ones = grid.count { |row| row[j] == 1 }
    ans += [ones, m - ones].max * (1 << (n - 1 - j))
  end
  ans
end
"""

FILES["0862_shortest_subarray_with_sum_at_least_k"] = header("0862", "Shortest Subarray with Sum at Least K", "shortest-subarray-with-sum-at-least-k") + """# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def shortest_subarray(nums, k)
  n = nums.length
  prefix = Array.new(n + 1, 0)
  nums.each_with_index { |x, i| prefix[i + 1] = prefix[i] + x }
  dq = []
  ans = n + 1
  prefix.each_with_index do |p, i|
    while !dq.empty? && p - prefix[dq[0]] >= k
      ans = [ans, i - dq.shift].min
    end
    dq.pop while !dq.empty? && p <= prefix[dq[-1]]
    dq << i
  end
  ans <= n ? ans : -1
end
"""

FILES["0863_all_nodes_distance_k_in_binary_tree"] = header("0863", "All Nodes Distance K in Binary Tree", "all-nodes-distance-k-in-binary-tree") + TREE + """
# @param {TreeNode} root
# @param {TreeNode} target
# @param {Integer} k
# @return {Integer[]}
def distance_k(root, target, k)
  graph = Hash.new { |h, k| h[k] = [] }

  build = lambda do |node, parent|
    return if node.nil?

    if parent
      graph[node] << parent
      graph[parent] << node
    end
    build.call(node.left, node)
    build.call(node.right, node)
  end

  build.call(root, nil)

  unless target.respond_to?(:val)
    find = lambda do |node|
      return nil if node.nil?
      return node if node.val == target

      find.call(node.left) || find.call(node.right)
    end
    target = find.call(root)
  end

  queue = [[target, 0]]
  seen = { target => true }
  ans = []
  until queue.empty?
    node, dist = queue.shift
    if dist == k
      ans << node.val
      next
    end
    graph[node].each do |nei|
      next if seen[nei]

      seen[nei] = true
      queue << [nei, dist + 1]
    end
  end
  ans
end
"""

FILES["0864_shortest_path_to_get_all_keys"] = header("0864", "Shortest Path to Get All Keys", "shortest-path-to-get-all-keys") + """# @param {String[]} grid
# @return {Integer}
def shortest_path_all_keys(grid)
  m = grid.length
  n = grid[0].length
  all_keys = 0
  start = [0, 0]
  m.times do |i|
    n.times do |j|
      if grid[i][j] == "@"
        start = [i, j]
      elsif grid[i][j] >= "a" && grid[i][j] <= "f"
        all_keys |= 1 << (grid[i][j].ord - 97)
      end
    end
  end

  queue = [[start[0], start[1], 0, 0]]
  seen = { [start[0], start[1], 0] => true }
  until queue.empty?
    r, c, mask, dist = queue.shift
    return dist if mask == all_keys

    [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]].each do |nr, nc|
      next unless nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] != "#"

      cell = grid[nr][nc]
      nmask = mask
      nmask |= 1 << (cell.ord - 97) if cell >= "a" && cell <= "f"
      next if cell >= "A" && cell <= "F" && (mask & (1 << (cell.ord - 65))).zero?

      state = [nr, nc, nmask]
      next if seen[state]

      seen[state] = true
      queue << [nr, nc, nmask, dist + 1]
    end
  end
  -1
end
"""

FILES["0865_smallest_subtree_with_all_the_deepest_nodes"] = header("0865", "Smallest Subtree with all the Deepest Nodes", "smallest-subtree-with-all-the-deepest-nodes") + TREE + """
# @param {TreeNode} root
# @return {TreeNode}
def subtree_with_all_deepest(root)
  dfs = lambda do |node|
    return [0, nil] if node.nil?

    ld, ln = dfs.call(node.left)
    rd, rn = dfs.call(node.right)
    return [ld + 1, ln] if ld > rd
    return [rd + 1, rn] if rd > ld

    [ld + 1, node]
  end

  dfs.call(root)[1]
end
"""

FILES["0866_prime_palindrome"] = header("0866", "Prime Palindrome", "prime-palindrome") + """# @param {Integer} n
# @return {Integer}
def prime_palindrome(n)
  is_prime = lambda do |x|
    return false if x < 2
    return x == 2 if x.even?

    d = 3
    while d * d <= x
      return false if x % d == 0

      d += 2
    end
    true
  end

  pals = lambda do
    (1..5).each do |length|
      start = 10**(length - 1)
      finish = 10**length
      (start...finish).each do |root|
        s = root.to_s
        pal = (s + s[0, [s.length - 1, 1].max].reverse).to_i
        return pal if pal >= n && is_prime.call(pal)
      end
    end
    0
  end

  return 2 if n <= 2
  return 3 if n <= 3
  return 5 if n <= 5
  return 7 if n <= 7
  return 11 if n <= 11

  pals.call
end
"""

FILES["0867_transpose_matrix"] = header("0867", "Transpose Matrix", "transpose-matrix") + """# @param {Integer[][]} matrix
# @return {Integer[][]}
def transpose(matrix)
  matrix.transpose
end
"""

FILES["0868_binary_gap"] = header("0868", "Binary Gap", "binary-gap") + """# @param {Integer} n
# @return {Integer}
def binary_gap(n)
  last = -1
  ans = 0
  bit = 0
  while n.positive?
    if n & 1 == 1
      ans = [ans, bit - last].max if last != -1
      last = bit
    end
    n >>= 1
    bit += 1
  end
  ans
end
"""

FILES["0869_reordered_power_of_2"] = header("0869", "Reordered Power of 2", "reordered-power-of-2") + """# @param {Integer} n
# @return {Boolean}
def reordered_power_of2(n)
  target = n.to_s.chars.sort
  (0...31).any? { |i| (1 << i).to_s.chars.sort == target }
end
"""

FILES["0870_advantage_shuffle"] = header("0870", "Advantage Shuffle", "advantage-shuffle") + """# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
def advantage_count(nums1, nums2)
  sorted1 = nums1.sort
  ans = Array.new(nums1.length, 0)
  nums2.each_with_index.sort_by { |val, _| -val }.each do |val, i|
    ans[i] = sorted1[-1] > val ? sorted1.pop : sorted1.shift
  end
  ans
end
"""

FILES["0871_minimum_number_of_refueling_stops"] = header("0871", "Minimum Number of Refueling Stops", "minimum-number-of-refueling-stops") + """class MaxHeap
  def initialize
    @a = []
  end

  def empty?
    @a.empty?
  end

  def push(item)
    @a << item
    i = @a.size - 1
    while i.positive?
      p = (i - 1) / 2
      break if @a[p] >= @a[i]

      @a[p], @a[i] = @a[i], @a[p]
      i = p
    end
  end

  def pop
    top = @a[0]
    last = @a.pop
    return top if @a.empty?

    @a[0] = last
    i = 0
    loop do
      l = i * 2 + 1
      r = l + 1
      break if l >= @a.size

      largest = r < @a.size && @a[r] > @a[l] ? r : l
      break if @a[i] >= @a[largest]

      @a[i], @a[largest] = @a[largest], @a[i]
      i = largest
    end
    top
  end
end

# @param {Integer} target
# @param {Integer} start_fuel
# @param {Integer[][]} stations
# @return {Integer}
def min_refuel_stops(target, start_fuel, stations)
  pq = MaxHeap.new
  stations = stations + [[target, 0]]
  ans = 0
  prev = 0
  fuel = start_fuel
  stations.each do |pos, gas|
    fuel -= pos - prev
    while !pq.empty? && fuel < 0
      fuel += pq.pop
      ans += 1
    end
    return -1 if fuel < 0

    pq.push(gas)
    prev = pos
  end
  ans
end
"""

FILES["0872_leaf_similar_trees"] = header("0872", "Leaf-Similar Trees", "leaf-similar-trees") + TREE + """
# @param {TreeNode} root1
# @param {TreeNode} root2
# @return {Boolean}
def leaf_similar(root1, root2)
  leaves = lambda do |node|
    return [] if node.nil?
    return [node.val] if node.left.nil? && node.right.nil?

    leaves.call(node.left) + leaves.call(node.right)
  end

  leaves.call(root1) == leaves.call(root2)
end
"""

FILES["0873_length_of_longest_fibonacci_subsequence"] = header("0873", "Length of Longest Fibonacci Subsequence", "length-of-longest-fibonacci-subsequence") + """# @param {Integer[]} arr
# @return {Integer}
def len_longest_fib_subseq(arr)
  index = {}
  arr.each_with_index { |x, i| index[x] = i }
  n = arr.length
  dp = Array.new(n) { Array.new(n, 2) }
  ans = 0
  n.times do |j|
    j.times do |i|
      k = index[arr[j] - arr[i]]
      if !k.nil? && k < i
        dp[i][j] = dp[k][i] + 1
        ans = dp[i][j] if dp[i][j] > ans
      end
    end
  end
  ans >= 3 ? ans : 0
end
"""

FILES["0874_walking_robot_simulation"] = header("0874", "Walking Robot Simulation", "walking-robot-simulation") + """# @param {Integer[]} commands
# @param {Integer[][]} obstacles
# @return {Integer}
def robot_sim(commands, obstacles)
  blocked = {}
  obstacles.each { |x, y| blocked[[x, y]] = true }
  dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  x = 0
  y = 0
  d = 0
  best = 0
  commands.each do |cmd|
    if cmd == -1
      d = (d + 1) % 4
    elsif cmd == -2
      d = (d + 3) % 4
    else
      dx, dy = dirs[d]
      cmd.times do
        nx = x + dx
        ny = y + dy
        break if blocked[[nx, ny]]

        x = nx
        y = ny
      end
      best = [best, x * x + y * y].max
    end
  end
  best
end
"""

FILES["0875_koko_eating_bananas"] = header("0875", "Koko Eating Bananas", "koko-eating-bananas") + """# @param {Integer[]} piles
# @param {Integer} h
# @return {Integer}
def min_eating_speed(piles, h)
  lo = 1
  hi = piles.max
  while lo < hi
    mid = (lo + hi) / 2
    hours = piles.sum { |p| (p + mid - 1) / mid }
    if hours <= h
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
"""

FILES["0876_middle_of_the_linked_list"] = header("0876", "Middle of the Linked List", "middle-of-the-linked-list") + LISTN + """
# @param {ListNode} head
# @return {ListNode}
def middle_node(head)
  slow = head
  fast = head
  while fast && fast.next
    slow = slow.next
    fast = fast.next.next
  end
  slow
end
"""

FILES["0877_stone_game"] = header("0877", "Stone Game", "stone-game") + """# @param {Integer[]} piles
# @return {Boolean}
def stone_game(_piles)
  true
end
"""

FILES["0878_nth_magical_number"] = header("0878", "Nth Magical Number", "nth-magical-number") + """# @param {Integer} n
# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def nth_magical_number(n, a, b)
  mod = 10**9 + 7
  lcm = a / a.gcd(b) * b
  lo = 1
  hi = n * [a, b].min
  while lo < hi
    mid = (lo + hi) / 2
    if mid / a + mid / b - mid / lcm >= n
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo % mod
end
"""

FILES["0879_profitable_schemes"] = header("0879", "Profitable Schemes", "profitable-schemes") + """# @param {Integer} n
# @param {Integer} min_profit
# @param {Integer[]} group
# @param {Integer[]} profit
# @return {Integer}
def profitable_schemes(n, min_profit, group, profit)
  mod = 10**9 + 7
  dp = Array.new(n + 1) { Array.new(min_profit + 1, 0) }
  dp[0][0] = 1
  group.zip(profit).each do |members, p|
    n.downto(members) do |people|
      min_profit.downto(0) do |prof|
        np = [min_profit, prof + p].min
        dp[people][np] = (dp[people][np] + dp[people - members][prof]) % mod
      end
    end
  end
  (0..n).sum { |people| dp[people][min_profit] } % mod
end
"""


def main():
    written = 0
    for folder, content in FILES.items():
        if content.startswith("\ufeff"):
            raise SystemExit(f"BOM in {folder}")
        path = ROOT / folder / "solution.rb"
        path.write_text(content, encoding="utf-8", newline="\n")
        written += 1
        print(f"wrote {folder}")
    print(f"total {written}")


if __name__ == "__main__":
    main()
