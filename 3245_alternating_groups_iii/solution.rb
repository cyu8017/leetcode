# LeetCode 3245 - Alternating Groups III
# https://leetcode.com/problems/alternating-groups-iii/

class SegTree
  def initialize(n_)
    @n = n_
    @tree_interval_counts = Array.new(4 * n_, 0)
    @tree_interval_lengths = Array.new(4 * n_, 0)
  end

  def add(i, val)
    add_rec(0, 0, @n - 1, i, val)
  end

  def add_rec(tree_index, lo, hi, i, val)
    if lo == hi
      @tree_interval_counts[tree_index] += val
      @tree_interval_lengths[tree_index] = @tree_interval_counts[tree_index] * i
      return
    end
    mid = (lo + hi) >> 1
    if i <= mid
      add_rec(2 * tree_index + 1, lo, mid, i, val)
    else
      add_rec(2 * tree_index + 2, mid + 1, hi, i, val)
    end
    @tree_interval_counts[tree_index] = @tree_interval_counts[2 * tree_index + 1] + @tree_interval_counts[2 * tree_index + 2]
    @tree_interval_lengths[tree_index] = @tree_interval_lengths[2 * tree_index + 1] + @tree_interval_lengths[2 * tree_index + 2]
  end

  def query_interval_counts(i)
    query(@tree_interval_counts, 0, 0, @n - 1, i, @n - 1)
  end

  def query_interval_lengths(i)
    query(@tree_interval_lengths, 0, 0, @n - 1, i, @n - 1)
  end

  def query(tree, tree_index, lo, hi, i, j)
    return tree[tree_index] if i <= lo && hi <= j
    return 0 if j < lo || hi < i
    mid = (lo + hi) >> 1
    query(tree, tree_index * 2 + 1, lo, mid, i, j) + query(tree, tree_index * 2 + 2, mid + 1, hi, i, j)
  end
end

# @param {Integer[]} colors
# @param {Integer[][]} queries
# @return {Integer[]}
def number_of_alternating_groups(colors, queries)
  n = colors.length
  ans = []
  arr = Array.new(2 * n - 1, 0)
  (0...n).each { |i| arr[i] = colors[i] }
  (0...n - 1).each { |i| arr[n + i] = colors[i] }
  pack = lambda { |l, r| (l << 32) | (r & 0xFFFFFFFF) }
  unpack_l = lambda { |v| v >> 32 }
  unpack_r = lambda { |v| v & 0xFFFFFFFF }
  tree = SegTree.new(2 * n - 1)
  intervals = {}
  insert = lambda do |l, r|
    intervals[pack.call(l, r)] = true
    tree.add(r - l + 1, 1) if l < n
  end
  remove = lambda do |l, r|
    intervals.delete(pack.call(l, r))
    tree.add(r - l + 1, -1) if l < n
  end
  find_interval = lambda do |target|
    best_l = best_r = -1
    intervals.each_key do |k|
      kl = unpack_l.call(k)
      kr = unpack_r.call(k)
      if kl <= target && target <= kr && kl > best_l
        best_l = kl
        best_r = kr
      end
    end
    [best_l, best_r]
  end
  get_num = lambda do |sz|
    num_intervals = tree.query_interval_counts(sz)
    sum_intervals = tree.query_interval_lengths(sz)
    num_alternating_groups = sum_intervals - num_intervals * sz + num_intervals
    l, r = find_interval.call(n)
    return num_alternating_groups if l < 0 || l >= n || r - l + 1 < sz
    if r >= n
      non_duplicate_groups = n - l
      num_groups = (r - l + 1) - sz + 1
      extra = num_groups - non_duplicate_groups
      num_alternating_groups -= extra if extra > 0
    end
    num_alternating_groups
  end
  update = lambda do |index, color|
    return if arr[index] == color
    arr[index] = color
    start, end_ = find_interval.call(index)
    remove.call(start, end_)
    if start < index && index < end_
      insert.call(start, index - 1)
      insert.call(index, index)
      insert.call(index + 1, end_)
      return
    end
    insert.call(start + 1, end_) if start == index && index < end_
    insert.call(start, end_ - 1) if start < index && index == end_
    ns = ne = index
    loop do
      merged = false
      intervals.keys.each do |k|
        kl = unpack_l.call(k)
        kr = unpack_r.call(k)
        if kr + 1 == ns && arr[kr] != arr[ns]
          remove.call(kl, kr)
          ns = kl
          merged = true
          break
        end
      end
      break unless merged
    end
    loop do
      merged = false
      intervals.keys.each do |k|
        kl = unpack_l.call(k)
        kr = unpack_r.call(k)
        if kl == ne + 1 && arr[kl] != arr[ne]
          remove.call(kl, kr)
          ne = kr
          merged = true
          break
        end
      end
      break unless merged
    end
    insert.call(ns, ne)
  end
  st = 0
  (1...(2 * n - 1)).each do |i|
    if arr[i] == arr[i - 1]
      insert.call(st, i - 1)
      st = i
    end
  end
  insert.call(st, 2 * n - 2)
  queries.each do |query|
    if query[0] == 1
      ans << get_num.call(query[1])
    else
      index = query[1]
      color = query[2]
      if arr[index] != color
        update.call(index, color)
        update.call(index + n, color) if index < n - 1
      end
    end
  end
  ans
end
