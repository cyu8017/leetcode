# LeetCode 3923 - Minimum Generations to Target Point
# https://leetcode.com/problems/minimum-generations-to-target-point/

# @param {Integer[][]} points
# @param {Integer[]} target
# @return {Integer}
def min_generations(points, target)
  target_key = "#{target[0]},#{target[1]},#{target[2]}"
  generation = {}
  all_pts = []
  points.each do |values|
    key = "#{values[0]},#{values[1]},#{values[2]}"
    generation[key] = 0
    all_pts << values.dup
  end
  return generation[target_key] if generation.key?(target_key)
  current = 1
  loop do
    limit = all_pts.length
    added = []
    (0...limit).each do |i|
      ((i + 1)...limit).each do |j|
        pi = all_pts[i]
        pj = all_pts[j]
        next if pi[0] == pj[0] && pi[1] == pj[1] && pi[2] == pj[2]
        p = [(pi[0] + pj[0]) / 2, (pi[1] + pj[1]) / 2, (pi[2] + pj[2]) / 2]
        key = "#{p[0]},#{p[1]},#{p[2]}"
        unless generation.key?(key)
          generation[key] = current
          added << p
        end
      end
    end
    return generation[target_key] if generation.key?(target_key)
    return -1 if added.empty?
    added.each { |p| all_pts << p }
    current += 1
  end
end
