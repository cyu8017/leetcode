# LeetCode 3310 - Remove Methods From Project
# https://leetcode.com/problems/remove-methods-from-project/

# @param {Integer} n
# @param {Integer} k
# @param {Integer[][]} invocations
# @return {Integer[]}
def remaining_methods(n, k, invocations)
  g = Array.new(n) { [] }
  invocations.each { |e| g[e[0]] << e[1] }
  sus = Array.new(n, false)
  stack = [k]
  until stack.empty?
    u = stack.pop
    next if sus[u]

    sus[u] = true
    g[u].each { |v| stack << v }
  end
  invocations.each do |e|
    return (0...n).to_a if !sus[e[0]] && sus[e[1]]
  end
  (0...n).select { |i| !sus[i] }
end
