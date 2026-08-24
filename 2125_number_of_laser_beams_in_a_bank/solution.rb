# LeetCode 2125 - Number of Laser Beams in a Bank
# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

# @param {String[]} bank
# @return {Integer}
def number_of_beams(bank)
  ans = 0
  prev = 0
  bank.each do |row|
    cnt = row.count("1")
    if cnt > 0
      ans += prev * cnt
      prev = cnt
    end
  end
  ans
end
