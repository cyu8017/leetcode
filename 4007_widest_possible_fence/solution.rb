# LeetCode 4007 - Widest Possible Fence
# https://leetcode.com/problems/widest-possible-fence/

# @param {Integer[]} planks
# @return {Integer}
def maximum_width(planks)
  cnt = {}
  planks.each { |x| cnt[x] = cnt.fetch(x, 0) + 1 }
  t = {}
  ans = 0
  cnt.each do |x, v1|
    t[x] = t.fetch(x, 0) + v1
    ans = t[x] if t[x] > ans
    t[x * 2] = t.fetch(x * 2, 0) + v1 / 2
    ans = t[x * 2] if t[x * 2] > ans
    cnt.each do |y, v2|
      next unless y > x
      key = x + y
      t[key] = t.fetch(key, 0) + [v1, v2].min
      ans = t[key] if t[key] > ans
    end
  end
  ans
end
