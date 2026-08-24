# LeetCode 3377 - Digit Operations to Make Two Integers Equal
# https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/

# @param {Integer} n
# @return {Boolean[]}
def sieve_primes(n)
  is_p = Array.new(n, false)
  (2...n).each { |i| is_p[i] = true }
  i = 2
  while i * i < n
    if is_p[i]
      j = i * i
      while j < n
        is_p[j] = false
        j += i
      end
    end
    i += 1
  end
  is_p
end

# @param {Integer} n
# @param {Integer} m
# @return {Integer}
def min_operations(n, m)
  is_prime = sieve_primes(100_000)
  return -1 if is_prime[n]

  dist = Array.new(100_000, -1)
  pq = [[n, n]]
  dist[n] = n
  until pq.empty?
    pq.sort_by! { |a| a[0] }
    cost, val = pq.shift
    next if cost != dist[val]
    return cost if val == m

    s = val.to_s.chars
    s.length.times do |i|
      orig = s[i]
      [-1, 1].each do |d|
        nd = (orig.ord - 48) + d
        next if nd < 0 || nd > 9
        next if i == 0 && nd == 0 && s.length > 1

        s[i] = nd.to_s
        nv = s.join.to_i
        s[i] = orig
        next if is_prime[nv]

        nc = cost + nv
        if dist[nv] == -1 || nc < dist[nv]
          dist[nv] = nc
          pq << [nc, nv]
        end
      end
    end
  end
  -1
end
