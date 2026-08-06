# LeetCode 1500 - Design a File Sharing System
# https://leetcode.com/problems/design-a-file-sharing-system/

require 'set'

class FileSharing
  def initialize(_m)
    @owners = Hash.new { |h, k| h[k] = Set.new }
    @chunks = {}
    @free = []
    @next_id = 1
  end

  def join(owned_chunks)
    if @free.empty?
      user = @next_id
      @next_id += 1
    else
      @free.sort!
      user = @free.shift
    end
    @chunks[user] = Set.new(owned_chunks)
    owned_chunks.each { |chunk| @owners[chunk].add(user) }
    user
  end

  def leave(user_id)
    (@chunks.delete(user_id) || []).each { |chunk| @owners[chunk].delete(user_id) }
    @free << user_id
    nil
  end

  def request(user_id, chunk_id)
    users = @owners[chunk_id].to_a.sort
    unless users.empty?
      @chunks[user_id].add(chunk_id)
      @owners[chunk_id].add(user_id)
    end
    users
  end
end
