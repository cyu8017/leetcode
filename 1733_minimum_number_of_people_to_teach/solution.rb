# LeetCode 1733 - Minimum Number of People to Teach
# https://leetcode.com/problems/minimum-number-of-people-to-teach/

# @param {Integer} n
# @param {Integer[][]} languages
# @param {Integer[][]} friendships
# @return {Integer}
def minimum_teachings(n, languages, friendships)
  known = languages.map { |items| items.to_h { |lang| [lang, true] } }
  need = {}
  friendships.each do |u, v|
    shares = known[u - 1].keys.any? { |lang| known[v - 1].key?(lang) }
    unless shares
      need[u - 1] = true
      need[v - 1] = true
    end
  end
  return 0 if need.empty?
  (1..n).map { |lang| need.keys.count { |user| !known[user].key?(lang) } }.min
end
