# LeetCode 0588 - Design In-Memory File System
# https://leetcode.com/problems/design-in-memory-file-system/

class FileSystem
  def initialize
    @root = {}
  end

  def ls(path)
    if path == "/"
      return @root.keys.sort
    end

    parts = parts_of(path)
    node = @root
    parts.each { |part| node = node[part] }

    return [parts[-1]] if node.is_a?(String)

    node.keys.sort
  end

  def mkdir(path)
    node = @root
    parts_of(path).each do |part|
      node[part] ||= {}
      node = node[part]
    end
    nil
  end

  def add_content_to_file(file_path, content)
    parts = parts_of(file_path)
    node = @root
    parts[0...-1].each do |part|
      node[part] ||= {}
      node = node[part]
    end

    name = parts[-1]
    existing = node[name] || ""
    node[name] = existing + content
    nil
  end

  def read_content_from_file(file_path)
    node = @root
    parts_of(file_path).each { |part| node = node[part] }
    node
  end

  private

  def parts_of(path)
    path.split("/").reject(&:empty?)
  end
end
