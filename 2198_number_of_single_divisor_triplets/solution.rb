# LeetCode 2198 - Number of Single Divisor Triplets
# https://leetcode.com/problems/number-of-single-divisor-triplets/

# @param {Integer[]} nums
# @return {Integer}
def single_divisor_triplet(nums)
  freq = Array.new(101, 0)
  nums.each { |x| freq[x] += 1 }
  ans = 0
  (1..100).each do |a|
    next if freq[a].zero?

    (a..100).each do |b|
      next if freq[b].zero?

      (b..100).each do |c|
        next if freq[c].zero?

        s = a + b + c
        cnt = 0
        cnt += 1 if s % a == 0
        cnt += 1 if s % b == 0
        cnt += 1 if s % c == 0
        next if cnt != 1

        ans += if a == b && b == c
                 freq[a] * (freq[a] - 1) * (freq[a] - 2)
               elsif a == b
                 freq[a] * (freq[a] - 1) * freq[c] * 3
               elsif b == c
                 freq[b] * (freq[b] - 1) * freq[a] * 3
               elsif a == c
                 freq[a] * (freq[a] - 1) * freq[b] * 3
               else
                 freq[a] * freq[b] * freq[c] * 6
               end
      end
    end
  end
  ans
end

alias solve single_divisor_triplet
