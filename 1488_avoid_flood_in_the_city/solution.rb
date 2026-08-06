# LeetCode 1488 - Avoid Flood In The City
# https://leetcode.com/problems/avoid-flood-in-the-city/

def avoid_flood(rains)
  ans = Array.new(rains.length, -1)
  full = {}
  dry = []
  rains.each_with_index do |lake, i|
    if lake == 0
      dry << i
      ans[i] = 1
    else
      if full.key?(lake)
        j = dry.bsearch_index { |x| x > full[lake] }
        return [] if j.nil?
        ans[dry.delete_at(j)] = lake
      end
      full[lake] = i
    end
  end
  ans
end
