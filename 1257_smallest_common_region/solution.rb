# LeetCode 1257 - Smallest Common Region
# https://leetcode.com/problems/smallest-common-region/

require "set"

# @param {String[][]} regions
# @param {String} region1
# @param {String} region2
# @return {String}
def find_smallest_region(regions, region1, region2)
  parent = {}
  regions.each do |group|
    group[1..].each { |child| parent[child] = group[0] }
  end
  ancestors = Set.new
  while region1
    ancestors.add(region1)
    region1 = parent[region1]
  end
  region2 = parent[region2] until ancestors.include?(region2)
  region2
end
