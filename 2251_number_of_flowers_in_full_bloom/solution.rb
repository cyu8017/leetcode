# LeetCode 2251 - Number of Flowers in Full Bloom
# https://leetcode.com/problems/number-of-flowers-in-full-bloom/

# @param {Integer[][]} flowers
# @param {Integer[]} people
# @return {Integer[]}
def full_bloom_flowers(flowers, people)
  start = flowers.map { |f| f[0] }.sort
  finish = flowers.map { |f| f[1] }.sort

  upper_bound = lambda do |a, t|
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) >> 1
      if a[mid] <= t
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end

  lower_bound = lambda do |a, t|
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) >> 1
      if a[mid] < t
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end

  people.map { |t| upper_bound.call(start, t) - lower_bound.call(finish, t) }
end
