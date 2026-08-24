# LeetCode 3479 - Fruits Into Baskets III
# https://leetcode.com/problems/fruits-into-baskets-iii/

# @param {Integer[]} fruits
# @param {Integer[]} baskets
# @return {Integer}
def num_of_unplaced_fruits(fruits, baskets)
  n = baskets.length
  size = 1
  size <<= 1 while size < n
  tree = Array.new(size * 2, 0)
  (0...n).each { |i| tree[size + i] = baskets[i] }
  (size - 1).downto(1) { |i| tree[i] = [tree[i * 2], tree[i * 2 + 1]].max }
  find = nil
  find = lambda do |node, nl, nr, need|
    return -1 if tree[node] < need
    return nl if nl == nr

    mid = (nl + nr) / 2
    left = find.call(node * 2, nl, mid, need)
    return left if left != -1

    find.call(node * 2 + 1, mid + 1, nr, need)
  end
  update = lambda do |idx|
    p = size + idx
    tree[p] = -1
    p >>= 1
    while p > 0
      tree[p] = [tree[p * 2], tree[p * 2 + 1]].max
      p >>= 1
    end
  end
  unplaced = 0
  fruits.each do |f|
    idx = find.call(1, 0, size - 1, f)
    if idx == -1 || idx >= n
      unplaced += 1
    else
      update.call(idx)
    end
  end
  unplaced
end
