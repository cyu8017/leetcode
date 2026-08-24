# LeetCode 2213 - Longest Substring of One Repeating Character
# https://leetcode.com/problems/longest-substring-of-one-repeating-character/

Node = Struct.new(:l_char, :r_char, :size, :best, :l_len, :r_len)

# @param {String} s_
# @param {String} query_characters
# @param {Integer[]} query_indices
# @return {Integer[]}
def longest_repeating(s_, query_characters, query_indices)
  merge = lambda do |a, b|
    return b if a.nil? || a.size == 0
    return a if b.nil? || b.size == 0

    res = Node.new(a.l_char, b.r_char, a.size + b.size, [a.best, b.best].max, a.l_len, b.r_len)
    if a.r_char == b.l_char
      mid = a.r_len + b.l_len
      res.best = [res.best, mid].max
      res.l_len = a.size + b.l_len if a.l_len == a.size
      res.r_len = b.size + a.r_len if b.r_len == b.size
    end
    res
  end

  s = s_.chars
  n = s.length
  tree = Array.new(4 * n + 5)

  build = lambda do |idx, l, r|
    if l == r
      tree[idx] = Node.new(s[l], s[l], 1, 1, 1, 1)
      return
    end
    mid = (l + r) >> 1
    build.call(idx * 2, l, mid)
    build.call(idx * 2 + 1, mid + 1, r)
    tree[idx] = merge.call(tree[idx * 2], tree[idx * 2 + 1])
  end

  update = lambda do |idx, l, r, pos, ch|
    if l == r
      s[pos] = ch
      tree[idx] = Node.new(ch, ch, 1, 1, 1, 1)
      return
    end
    mid = (l + r) >> 1
    if pos <= mid
      update.call(idx * 2, l, mid, pos, ch)
    else
      update.call(idx * 2 + 1, mid + 1, r, pos, ch)
    end
    tree[idx] = merge.call(tree[idx * 2], tree[idx * 2 + 1])
  end

  build.call(1, 0, n - 1)
  ans = Array.new(query_indices.length)
  query_indices.each_with_index do |pos, i|
    update.call(1, 0, n - 1, pos, query_characters[i])
    ans[i] = tree[1].best
  end
  ans
end
