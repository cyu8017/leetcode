# LeetCode 2234 - Maximum Total Beauty of the Gardens
# https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/

# @param {Integer[]} flowers
# @param {Integer} new_flowers
# @param {Integer} target
# @param {Integer} full
# @param {Integer} partial
# @return {Integer}
def maximum_beauty(flowers, new_flowers, target, full, partial)
  n = flowers.length
  flowers = flowers.map { |x| [x, target].min }.sort
  s = flowers.sum
  if target * n - s <= new_flowers
    all_full = n * full
    leave_one = n >= 1 ? (n - 1) * full + (target - 1) * partial : 0
    return [all_full, leave_one].max
  end

  pref = Array.new(n + 1, 0)
  n.times { |i| pref[i + 1] = pref[i] + flowers[i] }
  ans = 0
  j = n - 1
  remain = new_flowers
  (0..n).each do |complete|
    if complete > 0
      need = target - flowers[n - complete]
      break if remain < need

      remain -= need
    end
    j -= 1 while j >= n - complete || (j >= 0 && flowers[j] * (j + 1) - pref[j + 1] > remain)
    partial_val = 0
    if j >= 0
      extra = (remain - (flowers[j] * (j + 1) - pref[j + 1])) / (j + 1)
      partial_val = flowers[j] + extra
      partial_val = target - 1 if partial_val >= target
    end
    ans = [ans, complete * full + partial_val * partial].max
  end
  ans
end
