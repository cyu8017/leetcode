# LeetCode 3881 - Direction Assignments with Exactly K Visible People
# https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/

N3881 = 100001
MOD3881 = 1_000_000_007
$fact3881 = nil
$inv_fact3881 = nil
$ready3881 = false

def qmi3881(a, k, p)
  res = 1
  while k != 0
    res = res * a % p if (k & 1) != 0
    k >>= 1
    a = a * a % p
  end
  res
end

def init3881
  return if $ready3881
  $fact3881 = Array.new(N3881, 0)
  $inv_fact3881 = Array.new(N3881, 0)
  $fact3881[0] = $inv_fact3881[0] = 1
  (1...N3881).each do |i|
    $fact3881[i] = $fact3881[i - 1] * i % MOD3881
    $inv_fact3881[i] = qmi3881($fact3881[i], MOD3881 - 2, MOD3881)
  end
  $ready3881 = true
end

def comb3881(n, k)
  $fact3881[n] * $inv_fact3881[k] % MOD3881 * $inv_fact3881[n - k] % MOD3881
end

# @param {Integer} n
# @param {Integer} pos
# @param {Integer} k
# @return {Integer}
def count_visible_people(n, pos, k)
  init3881
  l = pos
  r = n - pos - 1
  ans = 0
  (0..[k, l].min).each do |a|
    b = k - a
    if b <= r
      ans = (ans + 2 * comb3881(l, a) % MOD3881 * comb3881(r, b) % MOD3881) % MOD3881
    end
  end
  ans
end

alias qmi count_visible_people
