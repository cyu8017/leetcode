# LeetCode 3395 - Subsequences with a Unique Middle Mode I
# https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/

# @param {Integer[]} nums
# @return {Integer}
def subsequences_with_middle_mode(nums)
  mod = 1_000_000_007
  n = nums.length
  ans = 0
  (2...(n - 2)).each do |mid|
    (0...mid).each do |a|
      ((a + 1)...mid).each do |b|
        ((mid + 1)...n).each do |c|
          ((c + 1)...n).each do |d|
            ans += 1 if unique_mode_3395([nums[a], nums[b], nums[mid], nums[c], nums[d]])
          end
        end
      end
    end
  end
  ans % mod
end

def unique_mode_3395(a)
  freq = Hash.new(0)
  a.each { |x| freq[x] += 1 }
  best = 0
  cnt = 0
  freq.each_value do |f|
    if f > best
      best = f
      cnt = 1
    elsif f == best
      cnt += 1
    end
  end
  cnt == 1
end
