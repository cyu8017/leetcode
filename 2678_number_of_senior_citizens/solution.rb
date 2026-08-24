# LeetCode 2678 - Number of Senior Citizens
# https://leetcode.com/problems/number-of-senior-citizens/

# @param {String[]} details
# @return {Integer}
def count_seniors(details)
  ans = 0
  details.each do |d|
    age = (d[11].ord - 48) * 10 + (d[12].ord - 48)
    ans += 1 if age > 60
  end
  ans
end
