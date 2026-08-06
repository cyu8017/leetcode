# LeetCode 1395 - Count Number Of Teams
# https://leetcode.com/problems/count-number-of-teams/

def num_teams(rating)
  ans = 0
  rating.each_with_index do |x, j|
    ll = rating[0...j].count { |y| y < x }
    lg = j - ll
    rg = rating[(j + 1)..].count { |y| y > x }
    rl = rating.length - j - 1 - rg
    ans += ll * rg + lg * rl
  end
  ans
end
