# LeetCode 3629 - Minimum Jumps to Reach End via Prime Teleportation
# https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

# @param {Integer[]} nums
# @return {Integer}
def min_jumps(nums)
  fac = factors3629
  n = nums.length
  g = {}
  nums.each_with_index do |v, i|
    fac[v].each do |p|
      (g[p] ||= []) << i
    end
  end
  ans = 0
  vis = Array.new(n, false)
  vis[0] = true
  q = [0]
  loop do
    nq = []
    q.each do |i|
      return ans if i == n - 1

      idx = (g[nums[i]] || []).dup
      idx << i + 1
      idx << i - 1 if i > 0
      idx.each do |j|
        if j >= 0 && j < n && !vis[j]
          vis[j] = true
          nq << j
        end
      end
      g[nums[i]] = []
    end
    q = nq
    ans += 1
  end
end

def factors3629
  return $factors3629 if defined?($factors3629) && $factors3629

  mx = 1_000_001
  factors = Array.new(mx) { [] }
  (2...mx).each do |i|
    next unless factors[i].empty?

    i.step(mx - 1, i) { |j| factors[j] << i }
  end
  $factors3629 = factors
end
