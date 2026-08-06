# LeetCode 1494 - Parallel Courses Ii
# https://leetcode.com/problems/parallel-courses-ii/

def min_number_of_semesters(n, relations, k)
  prereq = Array.new(n, 0)
  relations.each { |a, b| prereq[b - 1] |= 1 << (a - 1) }
  full = (1 << n) - 1
  inf = 10**9
  dp = Array.new(1 << n, inf)
  dp[0] = 0
  (1 << n).times do |mask|
    next if dp[mask] == inf
    available = 0
    n.times do |c|
      available |= 1 << c if ((mask >> c) & 1) == 0 && (prereq[c] & mask) == prereq[c]
    end
    choices = []
    if available.to_s(2).count('1') <= k
      choices = [available]
    else
      sub = available
      while sub > 0
        choices << sub if sub.to_s(2).count('1') == k
        sub = (sub - 1) & available
      end
    end
    choices.each { |take| dp[mask | take] = [dp[mask | take], dp[mask] + 1].min }
  end
  dp[full]
end
