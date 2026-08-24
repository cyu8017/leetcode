# LeetCode 0851 - Loud and Rich
# https://leetcode.com/problems/loud-and-rich/

# @param {Integer[][]} richer
# @param {Integer[]} quiet
# @return {Integer[]}
def loud_and_rich(richer, quiet)
  n = quiet.length
  graph = Hash.new { |h, k| h[k] = [] }
  richer.each { |a, b| graph[b] << a }
  ans = Array.new(n, -1)

  dfs = lambda do |person|
    return ans[person] if ans[person] != -1

    best = person
    graph[person].each do |richer_person|
      cand = dfs.call(richer_person)
      best = cand if quiet[cand] < quiet[best]
    end
    ans[person] = best
  end

  n.times { |i| dfs.call(i) }
  ans
end
