# LeetCode 1352 - Product Of The Last K Numbers
# https://leetcode.com/problems/product-of-the-last-k-numbers/

class ProductOfNumbers
  def initialize
    @prefix = [1]
  end

  def add(num)
    if num == 0
      @prefix = [1]
    else
      @prefix << @prefix[-1] * num
    end
  end

  def get_product(k)
    return 0 if k >= @prefix.length
    @prefix[-1] / @prefix[-k - 1]
  end
end
