# LeetCode 2381 - Shifting Letters II
# https://leetcode.com/problems/shifting-letters-ii/

# @param {String} s
# @param {Integer[][]} shifts
# @return {String}
def shifting_letters(s, shifts)
  n = s.length
  diff = Array.new(n + 1, 0)
  shifts.each do |sh|
    d = sh[2] == 0 ? -1 : 1
    diff[sh[0]] += d
    diff[sh[1] + 1] -= d
  end
  arr = s.chars
  cur = 0
  (0...n).each do |i|
    cur = (cur + diff[i]) % 26
    cur += 26 if cur < 0
    arr[i] = (97 + (arr[i].ord - 97 + cur) % 26).chr
  end
  arr.join
end
