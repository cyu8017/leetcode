# LeetCode 3044 - Most Frequent Prime
# https://leetcode.com/problems/most-frequent-prime/

# @param {Integer[][]} mat
# @return {Integer}
def most_frequent_prime(mat)
  m = mat.length
  n = mat[0].length
  cnt = Hash.new(0)
  m.times do |i|
    n.times do |j|
      (-1..1).each do |a|
        (-1..1).each do |b|
          next if a == 0 && b == 0

          x = i + a
          y = j + b
          v = mat[i][j]
          while x >= 0 && x < m && y >= 0 && y < n
            v = v * 10 + mat[x][y]
            cnt[v] += 1 if prime?(v)
            x += a
            y += b
          end
        end
      end
    end
  end
  ans = -1
  mx = 0
  cnt.each do |key, value|
    if mx < value || (mx == value && ans < key)
      mx = value
      ans = key
    end
  end
  ans
end

def prime?(n)
  return false if n < 2

  i = 2
  while i <= n / i
    return false if n % i == 0

    i += 1
  end
  true
end
