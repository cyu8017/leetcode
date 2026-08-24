# LeetCode 3453 - Separate Squares I
# https://leetcode.com/problems/separate-squares-i/

# @param {Integer[][]} squares
# @return {Float}
def separate_squares(squares)
  total = 0
  squares.each do |sq|
    l = sq[2]
    total += l * l
  end
  area_below = lambda do |y|
    below = 0.0
    squares.each do |sq|
      yi = sq[1]
      l = sq[2]
      top = yi + l
      if y <= yi
        next
      elsif y >= top
        below += l * l
      else
        below += l * (y - yi)
      end
    end
    below
  end
  lo = 0.0
  hi = 2e9
  60.times do
    mid = (lo + hi) / 2.0
    if area_below.call(mid) * 2 < total
      lo = mid
    else
      hi = mid
    end
  end
  hi
end
