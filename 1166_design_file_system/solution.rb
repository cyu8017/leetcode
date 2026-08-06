# LeetCode 1166 - Design File System
# https://leetcode.com/problems/design-file-system/

class FileSystem
  def initialize
    @paths = { "" => -1 }
  end

  def create_path(path, value)
    return false if @paths.key?(path)
    parent = path.rpartition("/")[0]
    return false unless @paths.key?(parent)
    @paths[path] = value
    true
  end

  def get(path)
    @paths.fetch(path, -1)
  end
end
