# LeetCode 0838 - Push Dominoes
# https://leetcode.com/problems/push-dominoes/

# @param {String} dominoes
# @return {String}
def push_dominoes(dominoes)
  n = dominoes.length
  force = Array.new(n, 0)
  f = 0
  n.times do |i|
    if dominoes[i] == "R"
      f = n
    elsif dominoes[i] == "L"
      f = 0
    else
      f = [f - 1, 0].max
    end
    force[i] += f
  end
  f = 0
  (n - 1).downto(0) do |i|
    if dominoes[i] == "L"
      f = n
    elsif dominoes[i] == "R"
      f = 0
    else
      f = [f - 1, 0].max
    end
    force[i] -= f
  end
  force.map { |x| x > 0 ? "R" : x < 0 ? "L" : "." }.join
end
