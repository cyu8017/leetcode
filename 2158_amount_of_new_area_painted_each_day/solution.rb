# LeetCode 2158 - Amount of New Area Painted Each Day
# https://leetcode.com/problems/amount-of-new-area-painted-each-day/

# @param {Integer[][]} paint
# @return {Integer[]}
def amount_painted(paint)
  ans = Array.new(paint.length, 0)
  line = Array.new(50_001, 0)
  paint.each_with_index do |(start, finish), i|
    j = start
    while j < finish
      if line[j] == 0
        ans[i] += 1
        line[j] = finish
        j += 1
      else
        nxt = line[j]
        line[j] = [finish, nxt].max
        j = nxt
      end
    end
  end
  ans
end
