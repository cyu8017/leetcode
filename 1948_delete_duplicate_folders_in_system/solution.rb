# LeetCode 1948 - Delete Duplicate Folders in System
# https://leetcode.com/problems/delete-duplicate-folders-in-system/

# @param {String[][]} paths
# @return {String[][]}
def delete_duplicate_folder(paths)
  root = {}
  paths.each do |path|
    node = root
    path.each do |folder|
      node[folder] ||= {}
      node = node[folder]
    end
  end

  dup = {}
  serial_of = {}

  serialize = lambda do |node|
    return "" if node.empty?
    parts = node.keys.sort.map { |name| "#{name}(#{serialize.call(node[name])})" }
    serial = parts.join
    unless serial.empty?
      dup[serial] = dup.key?(serial)
      serial_of[node.object_id] = serial
    end
    serial
  end

  serialize.call(root)
  ans = []

  collect = lambda do |node, path|
    node.each do |name, child|
      serial = serial_of[child.object_id] || ""
      next if !serial.empty? && dup[serial]
      path << name
      ans << path.dup
      collect.call(child, path)
      path.pop
    end
  end

  collect.call(root, [])
  ans
end
