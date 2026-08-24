# LeetCode 2722 - Join Two Arrays by ID
# https://leetcode.com/problems/join-two-arrays-by-id/

# @param {Hash[]} arr1
# @param {Hash[]} arr2
# @return {Hash[]}
def join(arr1, arr2)
  by_id = {}
  arr1.each { |obj| by_id[obj["id"]] = obj.dup }
  arr2.each do |obj|
    if by_id.key?(obj["id"])
      by_id[obj["id"]].merge!(obj)
    else
      by_id[obj["id"]] = obj.dup
    end
  end
  by_id.values.sort_by { |o| o["id"] }
end
