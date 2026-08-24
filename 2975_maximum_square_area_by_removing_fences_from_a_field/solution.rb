# LeetCode 2975 - Maximum Square Area by Removing Fences From a Field
# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

# @param {Integer} m
# @param {Integer} n
# @param {Integer[]} h_fences
# @param {Integer[]} v_fences
# @return {Integer}
def maximize_square_area(m, n, h_fences, v_fences)
  mod = 1_000_000_007
  hg = fence_gaps(h_fences, m)
  vg = fence_gaps(v_fences, n)
  best = -1
  hg.each_key do |g|
    best = g if vg[g] && g > best
  end
  return -1 if best < 0

  best * best % mod
end

def fence_gaps(fences, bound)
  lst = [1] + fences + [bound]
  lst.sort!
  g = {}
  lst.length.times do |i|
    (i + 1...lst.length).each { |j| g[lst[j] - lst[i]] = true }
  end
  g
end
