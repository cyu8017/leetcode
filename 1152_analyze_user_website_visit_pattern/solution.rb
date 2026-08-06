# LeetCode 1152 - Analyze User Website Visit Pattern
# https://leetcode.com/problems/analyze-user-website-visit-pattern/

# @param {String[]} username
# @param {Integer[]} timestamp
# @param {String[]} website
# @return {String[]}
def most_visited_pattern(username, timestamp, website)
  visits = Hash.new { |h, k| h[k] = [] }
  username.each_index { |i| visits[username[i]] << [timestamp[i], website[i]] }
  scores = Hash.new(0)
  visits.each_value do |vs|
    sites = vs.sort_by(&:first).map(&:last)
    patterns = {}
    (0...sites.length).each do |i|
      ((i + 1)...sites.length).each do |j|
        ((j + 1)...sites.length).each do |k|
          patterns[[sites[i], sites[j], sites[k]]] = true
        end
      end
    end
    patterns.each_key { |p| scores[p] += 1 }
  end
  best = scores.min_by { |pattern, count| [-count, pattern] }[0]
  best
end
