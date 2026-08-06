# LeetCode 1467 - Probability Of A Two Boxes Having The Same Number Of Distinct Balls
# https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/

def get_probability(balls)
  half = balls.sum / 2
  good = total = 0
  comb = lambda do |n, k|
    return 0 if k < 0 || k > n
    res = 1
    k = [k, n - k].min
    (1..k).each { |i| res = res * (n - k + i) / i }
    res
  end
  dfs = nil
  dfs = lambda do |i, left, dl, ways|
    if i == balls.length
      if left == half
        total += ways
        good += ways if dl == 0
      end
      return
    end
    (0..balls[i]).each do |x|
      next if left + x > half
      dfs.call(i + 1, left + x, dl + (x > 0 ? 1 : 0) - (x < balls[i] ? 1 : 0), ways * comb.call(balls[i], x))
    end
  end
  dfs.call(0, 0, 0, 1)
  good.to_f / total
end
