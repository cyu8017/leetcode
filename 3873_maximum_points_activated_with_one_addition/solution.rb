# LeetCode 3873 - Maximum Points Activated with One Addition
# https://leetcode.com/problems/maximum-points-activated-with-one-addition/

# @param {Integer[][]} points
# @return {Integer}
def max_activated(points)
  p = {}
  size = {}
  find = nil
  find = lambda do |x|
    unless p.key?(x)
      p[x] = x
      size[x] = 1
    end
    p[x] = find.call(p[x]) if p[x] != x
    p[x]
  end
  unite = lambda do |a, b|
    pa = find.call(a)
    pb = find.call(b)
    return false if pa == pb
    if size[pa] > size[pb]
      p[pb] = pa
      size[pa] = size[pa] + size[pb]
    else
      p[pa] = pb
      size[pb] = size[pb] + size[pa]
    end
    true
  end
  m = 3_000_000_000
  points.each { |pt| unite.call(pt[0], pt[1] + m) }
  cnt = Hash.new(0)
  points.each { |pt| cnt[find.call(pt[0])] += 1 }
  mx1 = 0
  mx2 = 0
  cnt.each_value do |x|
    if mx1 < x
      mx2 = mx1
      mx1 = x
    elsif mx2 < x
      mx2 = x
    end
  end
  mx1 + mx2 + 1
end
